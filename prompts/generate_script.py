
def generate_scripts(model, content: str, language: str):
    text = (
        f"Based on the content provided below, please generate a dynamic and engaging press speech script in {language}. "
        f"Focus on delivering the main content with complete sentences and smooth transitions that create a flowing narrative. "
        f"Ensure the tone remains engaging yet professional, with a coherent structure that smoothly connects each idea. "
        f"Avoid any title, introductory phrases, opening remarks, or direct expressions of excitement or emotion. "
        f"The speech should be around 10 minutes, approximately 1300 to 1500 words, written in an accessible, flowing style that captivates the audience without abrupt or fragmented sentences. "
        f"Return only the script itself, with no additional information: {content}")


    response = model.generate([text])
    return response


