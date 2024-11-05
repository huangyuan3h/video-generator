import json


def get_keywords(model, content: str):
    global response_data
    text = """You will receive a piece of content. Based on this content, please provide a list of 5 visually appealing
     and popular hashtags that are optimized for finding high-quality videos and pictures, even if they are slightly
      less relevant to the content (though some connection should still be present). Return the response in JSON format,
       with the structure: { ‘keywords’: [‘keyword1’, ‘keyword2’, ‘keyword3’, ‘keyword4’, ‘keyword5’] }.
        Ensure these hashtags are concise, trending terms that lead to visually engaging media.
         If a keyword contains two words, remember to add space between. Return only the JSON content in English: """
    response = model.generate([text, content])
    try:
        response_data = json.loads(response)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)

    return response_data["keywords"]
