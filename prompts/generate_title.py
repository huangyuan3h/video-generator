

def generate_title(model, content: str, language: str):
    text = (f"Based on the script provided below, please generate a concise and attention-grabbing title in {language}. "
            f"The headline should reflect the core message of the content, all in a maximum of 10 words. "
            f"Return only the title itself, with no additional information or punctuation beyond the colon separator: {content}")
    response = model.generate([text])
    return response