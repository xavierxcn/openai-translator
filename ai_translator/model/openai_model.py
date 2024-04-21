from enum import Enum

import requests
import simplejson
import time
import os
import openai
from zhipuai import ZhipuAI

from ai_translator.model import Model
from ai_translator.utils import LOG
from openai import OpenAI


class AI(Enum):
    OPENAI = "openai"
    GLMAI = "glmai"


class OpenAIModel(Model):
    """
    openai 兼容模型
    """

    def __init__(self, ai: AI, model: str, api_key: str):
        self.model = model
        if not api_key:
            api_key = os.getenv("OPENAI_API_KEY")

        self.ai = ai
        if self.ai == AI.OPENAI:
            self.client = OpenAI(api_key=api_key)
        elif self.ai == AI.GLMAI:
            self.client = ZhipuAI(api_key=api_key)
        else:
            raise Exception(f"{self.ai} is not a valid model")

    def make_request(self, messages):
        attempts = 0
        while attempts < 3:
            try:
                response = self.client.chat.completions.create(
                        model=self.model,
                        messages=messages,
                        max_tokens=150,
                        temperature=0.1
                    )
                translation = response.choices[0].message.content.strip()
                return translation, True
            except openai.RateLimitError as e:
                attempts += 1
                if attempts < 3:
                    LOG.warning("Rate limit reached. Waiting for 60 seconds before retrying.")
                    time.sleep(60)
                else:
                    raise Exception("Rate limit reached. Maximum attempts exceeded.")
            except openai.APIConnectionError as e:
                print("The server could not be reached")
                print(
                    e.__cause__)  # an underlying Exception, likely raised within httpx.            except requests.exceptions.Timeout as e:
            except openai.APIStatusError as e:
                print("Another non-200-range status code was received")
                print(e.status_code)
                print(e.response)
            except Exception as e:
                raise Exception(f"发生了未知错误：{e}")
        return "", False
