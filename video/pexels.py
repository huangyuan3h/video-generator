import context
import requests


def search_video_by_keyword(query: str, size="medium", orientation='landscape'):
    """

    :param query: string
    :param size: large/medium/small
    :param orientation: landscape/portrait
    :return:
    """

    api_key = context.settings.pexel_key
    base_url = "https://api.pexels.com/videos/search"
    headers = {"Authorization": api_key, "Accept": "*/*", "User-Agent": "PostmanRuntime/7.42.0"}
    params = {"query": query, "per_page": 5, "size": size, "orientation": orientation}
    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
