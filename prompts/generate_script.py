

def generate_scripts(model, content: str, language:str):

    text = (f"Based on the content provided below, please generate a press speech script in {language}."
            f" Focus solely on delivering the main message, and avoid any introductory phrases like greetings "
            f"or closing remarks, such as ‘hello,’ ‘thank you,’ or ‘over.’"
            f" Return only the core script without any additional information or unnecessary filler phrases: {content}")
    response = model.generate([text])
    return response


