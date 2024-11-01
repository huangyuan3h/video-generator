from context import settings
from llm.GoogleGeminiClient import GoogleGeminiClient
from llm.OllamaClient import OllamaClient


def get_llm_client():
    llm_provider = settings.get("llm_provider")
    if llm_provider == "gemini":
        return GoogleGeminiClient()
    elif llm_provider == "ollama":
        return OllamaClient()

    return None
