import asyncio

from context.Context import VideoParameter
from llm.llm_client import get_llm_client
from prompts.generate_script import generate_scripts
from prompts.generate_title import generate_title
from prompts.get_keywords import get_keywords
from prompts.translator import translator
from task.images.cover_image import build_cover_image
from task.save_title_script import save_title_scripts
from task.subtitle import get_subtitle_obj
from task.task import create_new_task
from task.tts import text_to_speech, get_mp3_duration
from task.utils import get_audio_path, get_merged_movie_path, get_image_path, get_text_path
from task.video.merge_video import merge_videos_with_background_music_and_overlays
from task.video.pexels import get_videos_by_keywords, get_necessary_random_videos, download_video_list


def generate_video(params: VideoParameter):
    model = get_llm_client()

    if params.scripts is None:
        params.scripts = generate_scripts(model, params.content, params.language)
        print(params.scripts)

    if params.title is None:
        params.title = generate_title(model, params.scripts, params.language)
        print(params.title)

    taskId = create_new_task()
    params.taskId = taskId

    # save title and scripts
    save_title_scripts(params.title, params.scripts, get_text_path(taskId))

    asyncio.run(text_to_speech(params.scripts, params.voice_option, taskId))
    subtitle = get_subtitle_obj(taskId)

    seconds = get_mp3_duration(taskId)
    print(seconds)

    translated_content = translator(model, params.scripts, "English")

    print(translated_content)

    keywords = get_keywords(model, translated_content)

    print(keywords)

    video_orientations = params.video_orientations

    for orientation in video_orientations:
        build_cover_image(params.title, params.qr_url, keywords[0], taskId, orientation=orientation,
                          icon_path=params.icon_path)
        results = get_videos_by_keywords(keywords, orientation)

        results = get_necessary_random_videos(results, seconds)

        results_path = download_video_list(results)

        merge_videos_with_background_music_and_overlays(results_path, params.background_music,
                                                        narration_path=get_audio_path(taskId),
                                                        output_path=get_merged_movie_path(taskId, orientation),
                                                        subtitles=subtitle,
                                                        intro_image_path=get_image_path(taskId, orientation))
