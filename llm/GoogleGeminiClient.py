from context import settings
from llm.LLMClient import LLMClient


class GoogleGeminiClient(LLMClient):
    def __init__(self):
        import google.generativeai as genai
        google_gemini_api_key = settings.get("google_gemini_api_key")
        gemini_model_name = settings.get("gemini_model_name")
        genai.configure(api_key=google_gemini_api_key)
        model_name = gemini_model_name
        self.model = genai.GenerativeModel(model_name, safety_settings=[
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        ])

    def generate(self, prompt: [str]):
        response = self.model.generate_content(prompt)
        return response.text
