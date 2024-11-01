import json


def get_keywords(model, content: str):
    global response_data
    text = """You will receive a piece of content. Based on this content, please provide a list of 5 relevant 
    hashtags that are optimized for finding related videos. Return the response in JSON format, with the structure: {
    "keywords": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"]}. Ensure the hashtags are concise, 
    popular terms that align with the content and are commonly used for video searches.
    If the keyword is two words, remember to add space between.
    Ensure only return JSON content, but not markdown and the return keyword language should be English: """
    response = model.generate([text, content])
    try:
        response_data = json.loads(response)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)

    return response_data
