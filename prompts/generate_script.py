
def generate_scripts(model, content: str, language: str):
    text = (
        f"Based on the content provided below, generate a dynamic and engaging press speech script in {language}. "
        f"Directly address the main content without any form of introductory phrases, greetings (e.g., '各位媒体朋友'), "
        f"or thematic statements (e.g., '今天探讨...'). Start immediately with the core message and avoid any framing or contextual setup. "
        f"Write in complete sentences with smooth transitions to maintain a flowing narrative, ensuring the tone is professional and engaging. "
        f"The script should be around 10 minutes, approximately 1300 to 1500 words, and should read in an accessible, captivating style. "
        f"Return only the speech script, with no greetings, closings, or extra information: {content}")


    response = model.generate([text])
    return response


