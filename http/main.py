import os

from fastapi import FastAPI, File, UploadFile

from ai_translator.model import OpenAIModel
from ai_translator.translator.pdf_translator import PDFTranslator

app = FastAPI()
@app.get("/translate_pdf")
async def translate_pdf(
    file: bytes = File(), fileb: UploadFile = File(), dest_lang: str = "Chinese"
):

    # 保存到临时目录
    file_path = os.path.join(os.path.dirname(__file__), "temp.pdf")
    with open(file_path, "wb") as f:
        f.write(file)

    model = OpenAIModel(model="gpt-3.5-turbo", api_key=os.environ.get("OPENAI_API_KEY"))
    translator = PDFTranslator(model=model)
    translated = translator.translate_pdf(file_path, file_format="PDF", target_language=dest_lang)
    # 下载PDF文件
    with open(translated, "rb") as f:
        return f.read()


