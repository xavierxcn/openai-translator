from ai_translator.model import Model
from ai_translator.utils import LOG


class Translator:
    def __init__(self, model: Model):
        self.model = model

    def translate_text(self, text: str, source_language: str = "English", target_language: str = 'Chinese') -> str:
        prompt = self.model.make_text_messages(text, source_language, target_language)
        LOG.debug(prompt)
        translation, status = self.model.make_request(prompt)
        LOG.info(translation)
        return translation
