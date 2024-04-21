from ai_translator.book import ContentType



def first_message():
    return [
    {"role": "system", "content": "You play the role of an all-powerful translation assistant, proficient in various languages around the world, helping me translate the following text according to specified requirements."},
    ]

class Model:
    def make_text_messages(self, text: str, source_language: str, target_language: str) -> list:
        messages = first_message()
        messages.append({"role": "user", "content": f"translate {source_language} to {target_language}: {text}"})
        return messages

    def make_table_prompt(self, table: str, source_language: str, target_language: str) -> list:
        messages = first_message()
        messages.append({"role": "user", "content": (f"translate {source_language} to {target_language}，maintain spacing (spaces, separators), return in "
                f"table form：\n{table}")})
        return messages

    def translate_prompt(self, content, source_language: str, target_language: str) -> str:
        if content.content_type == ContentType.TEXT:
            return self.make_text_prompt(content.original, source_language, target_language)
        elif content.content_type == ContentType.TABLE:
            return self.make_table_prompt(content.get_original_as_str(), source_language, target_language)
        else:
            raise ValueError(f"Invalid content type. Expected {ContentType.TEXT}, but got {content.content_type}")

    def make_request(self, prompt):
        raise NotImplementedError("子类必须实现 make_request 方法")
