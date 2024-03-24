import io
from typing import Optional

from PIL import Image

from ai_translator.book import ContentType
from ai_translator.model import Model
from ai_translator.translator.pdf_parser import PDFParser
from ai_translator.translator.writer import Writer
from ai_translator.utils import LOG

class PDFTranslator:
    def __init__(self, model: Model):
        self.model = model
        self.pdf_parser = PDFParser()
        self.writer = Writer()

    def translate_pdf(self, pdf_file_path: str, file_format: str = 'PDF', target_language: str = '中文', output_file_path: str = None, pages: Optional[int] = None):
        self.book = self.pdf_parser.parse_pdf(pdf_file_path, pages)

        for page_idx, page in enumerate(self.book.pages):
            for content_idx, content in enumerate(page.contents):
                if content.content_type != ContentType.IMAGE:
                    prompt = self.model.translate_prompt(content, "",  target_language)
                    LOG.debug(prompt)
                    translation, status = self.model.make_request(prompt)
                    LOG.info(translation)
                else:
                    original = content.original
                    # 转 Image 类型
                    idata = io.BytesIO(original["stream"].rawdata)
                    image = Image.open(idata)
                    translation = image
                    status = True

                # Update the content in self.book.pages directly
                self.book.pages[page_idx].contents[content_idx].set_translation(translation, status)

        self.writer.save_translated_book(self.book, output_file_path, file_format)
        return output_file_path