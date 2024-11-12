from context import settings
from llm.LLMClient import LLMClient


class MoonshotClient(LLMClient):
    def __init__(self):
        from openai import OpenAI
        moonshot_api_key = settings.get("moonshot_api_key")

        self.model = OpenAI(
            api_key=moonshot_api_key,
            base_url="https://api.moonshot.cn/v1",
        )

    def generate(self, prompt: [str]):
        moonshot_model_name = settings.get("moonshot_model_name")
        messages = list(map(lambda s: {"role": "user", "content": s}, prompt))
        completion = self.model.chat.completions.create(
            model=moonshot_model_name,
            messages=messages,
            temperature=0.3,
        )
        return completion.choices[0].message.content