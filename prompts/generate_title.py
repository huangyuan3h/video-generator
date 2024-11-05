

def generate_title(model, content: str, language: str):
    text = (f"Based on the script provided below, please generate a concise and attention-grabbing title in {language}. "
            f"The title should contain a main headline and, if needed, a subtitle separated by a colon, to make the message clear and impactful. "
            f"The main headline should reflect the core message of the content, while the subtitle should add further context if appropriate. "
            f"The entire title should read naturally and be limited to 10 words. Return only the title with no extra information: {content}")
    response = model.generate([text])
    return response