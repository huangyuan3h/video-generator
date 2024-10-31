
from context import settings
from langchain.llms import GooglePalm
from google.generativeai.types import SafetySetting, HarmCategory, HarmBlockThreshold

google_gemini_api_key = settings.get("google_gemini_api_key")


safety_settings = [
    {
        "category": HarmCategory.HARM_CATEGORY_HARASSMENT,
        "threshold": HarmBlockThreshold.BLOCK_NONE,  # Or BLOCK_LOW, BLOCK_MEDIUM, BLOCK_HIGH
    },
    {
        "category": HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
]

llm = GooglePalm(
                 temperature=settings.get("temperature", 0.2),  # Optional: Temperature setting
                 api_key=google_gemini_api_key

                 )