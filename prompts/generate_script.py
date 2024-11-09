

def generate_scripts(model, content: str, language:str):

    text = (f"Based on the content provided below, please generate a direct, factual press speech script in {language} "
            f"that clearly conveys the main message without any introductory phrases, greetings (e.g., ‘尊敬的各位媒体朋友’),"
            f" or expressions of emotion (e.g., ‘我们很高兴地’). Focus solely on the main content"
            f" in a straightforward style, ensuring that all language is factual and to the point. "
            f" Make sure the speech script could be read around 3-5 minutes "
            f"Return only the script itself, with no greetings, closings, or additional information: {content}")
    response = model.generate([text])
    return response


