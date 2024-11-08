import requests

import context


def search_photo_by_keyword(query: str, size="medium", orientation="landscape", page=1, color=None,
                            per_page=5):
    """
    Search for photos on Pexels by keyword.

    :param color: image base color
    :param query: The search query (e.g., "Nature", "Ocean", "People").
    :param size: Minimum photo size ("large", "medium", or "small").
    :param orientation: Photo orientation ("landscape", "portrait", or "square").
    :param page: The page number for pagination.
    :param per_page: Number of results per page (default 15, max 80).
    :return: JSON response with the search results or None if an error occurred.
    """

    api_key = context.settings.pexel_key
    base_url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": api_key, "Accept": "*/*", "User-Agent": "PostmanRuntime/7.42.0"}
    params = {
        "query": query,
        "size": size,
        "orientation": orientation,
        "page": page,
        "color": color,
        "per_page": per_page
    }
    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


def get_top_photo(query, orientation="landscape"):
    result = search_photo_by_keyword(query, orientation)
    top_photo = result["photos"][0]
    url = top_photo["src"][orientation]
    return url
