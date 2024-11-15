import json


def get_keywords(model, content: str):
    global response_data
    text = """You will receive a piece of content. Based on this content, please provide a list of 5 visually appealing 
    and popular hashtags that are optimized for finding high-quality videos and pictures, 
    even if they are slightly less relevant to the content (though some connection should still be present).
    if the keywords contain more than 2 words remember to add space between.
    **Return the response in pure JSON format, without any additional text, in the following structure:**

    {
      "keywords": [
        "Egypt Revolution",
        "Arab Spring",
        "Social Justice",
        "Political Reform",
        "Global Inequality"
      ]
    }

    """

    response = model.generate([text, content])
    try:
        response_data = json.loads(response)
        print(response_data)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)

    return response_data["keywords"]
