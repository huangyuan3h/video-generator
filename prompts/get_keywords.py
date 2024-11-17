import json

import typing_extensions as typing

from nltk.tokenize import sent_tokenize

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

class Response(typing.TypedDict):
    keywords: list[str]


def get_keywords(model, content: str):
    global response_data
    text = """You will receive a piece of content. Based on this content, please provide a list of 5 visually appealing 
    and popular keywords that are optimized for finding high-quality videos and pictures, 
    even if they are slightly less relevant to the content (though some connection should still be present).
    If the keywords contain more than 2 words remember to add space between.
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

    def truncate_content(content, num_sentences=3):
        sentences = sent_tokenize(content)
        return ' '.join(sentences[:num_sentences])

    content_short = truncate_content(content, 5)

    response = model.generate([text, content_short], json=True, response_schema=Response)
    try:
        response_data = json.loads(response)
        print(response_data)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)

    return response_data["keywords"]
