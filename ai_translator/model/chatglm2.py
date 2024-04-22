from ai_translator.model import Model


from transformers import AutoTokenizer, AutoModel

class ChatGLM2Model(Model):
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True)
        self.model = AutoModel.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True).to("cuda")
        self.model = self.model.eval()

    def make_request(self, messages):
        history = []
        content = ""
        if len(messages) > 0:
            message = messages[-1]
            content = message["content"]
        response, history = self.model.chat(self.tokenizer, content, history=history)
        return response, True


