

def generate_title(model, content: str, language:str):

    text = (f"Based on the script provided below, please generate a concise, compelling, and attention-grabbing"
            f" title in {language} that reflects the core message of the content and is likely to attract interest."
            f" Return only the title itself, with no additional information: {content}")
    response = model.generate([text])
    return response