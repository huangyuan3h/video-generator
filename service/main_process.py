
import asyncio

from llm.llm_client import get_llm_client
from prompts.get_keywords import get_keywords
from prompts.translator import translator
from task.images.cover_image import build_cover_image
from task.subtitle import get_subtitle_obj
from task.task import create_new_task
from task.tts import text_to_speech, get_mp3_duration
from task.utils import get_audio_path, get_merged_movie_path, get_image_path
from task.video.merge_video import merge_videos_with_background_music_and_overlays
from task.video.pexels import get_videos_by_keywords, get_necessary_random_videos, download_video_list


def generate_video(text_content, title):
    taskId = create_new_task()

    voice_option = "zh-CN-YunxiNeural"

    music_path = "resources/background_music/Owls.mp3"

    asyncio.run(text_to_speech(text_content, voice_option, taskId))
    subtitle = get_subtitle_obj(taskId)

    seconds = get_mp3_duration(taskId)
    print(seconds)

    model = get_llm_client()

    translated_content = translator(model, text_content, "English")

    print(translated_content)

    keywords = get_keywords(model, translated_content)

    print(keywords)

    video_orientations = ["landscape", "portrait"]

    for orientation in video_orientations:

        build_cover_image(title, "https://north-path.it-t.xyz", keywords[0], taskId, orientation=orientation)
        results = get_videos_by_keywords(keywords, orientation)

        results = get_necessary_random_videos(results, seconds)

        results_path = download_video_list(results)

        merge_videos_with_background_music_and_overlays(results_path, music_path, narration_path=get_audio_path(taskId),
                                                        output_path=get_merged_movie_path(taskId, orientation),
                                                        subtitles=subtitle, intro_image_path=get_image_path(taskId, orientation))


