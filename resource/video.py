import setting
import requests


def download_video_by_keyword(query: str, size="medium", orientation='portrait'):
    api_key = setting.settings.pexel_key
    base_url = "https://api.pexels.com/videos/search"
    headers = {"Authorization": api_key, "Accept": "*/*", "User-Agent": "PostmanRuntime/7.42.0"}
    params = {"query": "nature", "per_page": 1, }
    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
