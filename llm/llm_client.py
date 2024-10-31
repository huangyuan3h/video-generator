from context import settings


def get_llm_client():
    llm_provider = settings.get("llm_provider")
    if llm_provider == "gemini":

        import google.generativeai as genai
        google_gemini_api_key = settings.get("google_gemini_api_key")
        genai.configure(api_key=google_gemini_api_key)
        model = genai.GenerativeModel("gemini-1.5-flash", safety_settings=[
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            ])
        return model

    return None
