from context import settings


class LLMClient:
    def generate(self, prompt: [str], json=False, response_schema=None):
        raise NotImplementedError("Subclasses should implement this method.")
