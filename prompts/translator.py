
def translator(model, content: str, language:str):

    text = f"translate the following content to {language}: {content}"
    response = model.generate([text])
    return response