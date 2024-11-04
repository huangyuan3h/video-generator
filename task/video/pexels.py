import os
import random

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


def get_videos_by_keywords(keywords: [str], orientation='landscape'):
    """

    :param orientation: "landscape"/"portrait"
    :param keywords:
    :return:
    """
    result = []

    for keyword in keywords:
        res = search_video_by_keyword(keyword, size="medium", orientation=orientation)

        result = result + res["videos"]

    result = map_the_video_file(result, orientation)

    return result


def is_landscape_size(video):
    return video["width"] == 1280 and video["height"] == 720


def is_portrait_size(video):
    return video["width"] == 720 and video["height"] == 1280


def video_2_file(video, orientation):
    files = video["video_files"]
    duration = video["duration"]
    video_files = list(filter(is_landscape_size if orientation == "landscape" else is_portrait_size, files))
    final_file = None if len(video_files) == 0 else video_files[0]
    if final_file is not None:
        final_file["duration"] = duration
    return final_file


def map_the_video_file(videos, orientation):
    """

    :param videos: [video object]
    :param orientation: "landscape"/"portrait"
    :return:
    """
    video_file_list = list(map(lambda v: video_2_file(v, orientation), videos))
    filtered_data = [x for x in video_file_list if x is not None]
    return filtered_data


def get_necessary_random_videos(videos, seconds):
    shuffled_landscape = random.sample(videos, len(videos))
    video_list = []
    counter = 0
    for v in shuffled_landscape:
        if counter < seconds:
            counter = counter + v["duration"]
            video_list.append(v)

    return video_list


def download_mp4(url: str, output_path: str):
    """
    Downloads an MP4 file from a given URL and saves it to the specified output path.

    Args:
        url (str): The URL of the MP4 file.
        output_path (str): The file path where the MP4 file will be saved.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for request errors

        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        print(f"Download complete: {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")


def download_video(video):
    id = video["id"]
    width = video["width"]
    height = video["height"]
    duration = video["duration"]
    url = video["link"]
    base_dir = "resources/pexels"
    path = os.path.join(base_dir, f"{id}_{width}x{height}_{duration}s.mp4")

    if os.path.isfile(path):
        return path

    download_mp4(url, path)

    return path


def download_video_list(videos):
    return list(map(download_video, videos))
