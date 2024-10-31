import os

import whisper

from task.utils import get_task_folder, get_audio_path, get_srt_path


def generate_srt_by_transcribed(transcribed, task_id):
    """
    将转录结果生成 SRT 字幕文件

    Args:
        transcribed: 转录结果
        task_id: 任务 ID
        save_path: 保存路径
    """
    srt_path = get_srt_path(task_id)
    with open(srt_path, 'wb') as temp_srt:
        for item in transcribed["segments"]:
            temp_srt.write(f"{item['id'] + 1}\n".encode("utf-8"))
            temp_srt.write(f"{item['start']} --> {item['end']}\n".encode("utf-8"))
            temp_srt.write(f"{item['text']}\n\n".encode("utf-8"))


def transcribe_audio_by_task_id(task_id, model_name="base"):
    model = whisper.load_model(model_name)
    result = model.transcribe(get_audio_path(task_id))
    return result


def generate_srt_by_task_id(task_id, model_name="base"):
    transcribed = transcribe_audio_by_task_id(task_id, model_name)
    generate_srt_by_transcribed(transcribed, task_id)