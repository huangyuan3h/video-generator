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


def get_videos_by_keywords(video_orientations: [str], keywords: [str]):
    """

    :param video_orientations: ["landscape", "portrait"]
    :param keywords:
    :return:
    """
    landscape = []
    portrait = []

    for orientation in video_orientations:
        for keyword in keywords:
            res = search_video_by_keyword(keyword, size="medium", orientation=orientation)
            if orientation == "landscape":
                landscape = landscape + res["videos"]
            elif orientation == "portrait":
                portrait = portrait + res["videos"]

    landscape = map_the_video_file(landscape, "landscape")
    portrait = map_the_video_file(portrait, "portrait")
    return landscape, portrait


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
