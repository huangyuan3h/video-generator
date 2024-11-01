from context import settings


class LLMClient:
    def generate(self, prompt: [str]):
        raise NotImplementedError("Subclasses should implement this method.")
