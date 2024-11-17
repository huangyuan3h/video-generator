import requests

from context import settings
from llm.LLMClient import LLMClient


class OllamaClient(LLMClient):
    def __init__(self):
        ollama_endpoint = settings.get("ollama_endpoint")
        ollama_model_name = settings.get("ollama_model_name")
        self.endpoint = ollama_endpoint
        self.model_name = ollama_model_name

    def generate(self, prompt: [str], json=False, response_schema=None):
        url = f"{self.endpoint}/api/chat"
        messages = [{"role": "user", "content": p} for p in prompt]
        payload = {
            "model": self.model_name,
            "messages": messages,
            "stream": False
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            responseJson = response.json()
            return responseJson["message"]['content']
        except requests.RequestException as e:
            print(f"Failed to connect to Ollama API: {e}")
            return None
