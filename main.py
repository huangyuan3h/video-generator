import random

from llm.llm_client import get_llm_client
from prompts.get_keywords import get_keywords
from prompts.translator import translator
from service.main_process import generate_video
from video.pexels import search_video_by_keyword, get_videos_by_keywords, get_necessary_random_videos

# generate_video()


# ['Quebec Immigration', 'PEQ', 'Canadian Immigration', 'Quebec French', 'Immigration Reform']


# response = search_video_by_keyword("Quebec Immigration")
#
# print(response)


keywords = ['Quebec Immigration', 'PEQ Program', 'Immigration Policy 2019', 'French Proficiency',
            'High Skilled Immigrants']

# search video from pexels


video_orientations = ["landscape", "portrait"]

landscape, portrait = get_videos_by_keywords(video_orientations, keywords)
seconds = 300

landscape = get_necessary_random_videos(landscape, seconds)
portrait = get_necessary_random_videos(portrait, seconds)


print(landscape, portrait)
