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


def transcribe_audio_by_task_id(task_id, model_name="large", language="zh"):
    model = whisper.load_model(model_name)
    result = model.transcribe(get_audio_path(task_id), language=language)

    return result


def generate_srt_by_task_id(task_id, model_name="base"):
    transcribed = transcribe_audio_by_task_id(task_id, model_name)
    generate_srt_by_transcribed(transcribed, task_id)


def get_subtitle_obj(task_id, model_name="base", max_text_length=20):
    transcribed = transcribe_audio_by_task_id(task_id, model_name)
    subtitles = []
    for item in transcribed["segments"]:
        text = item['text']
        start = item['start']
        duration = item['end'] - item['start']

        # 如果文本长度超过阈值，则将其拆分为两个部分
        if len(text) > max_text_length:
            midpoint = len(text) // 2  # 简单地在中间位置拆分
            first_part = text[:midpoint]
            second_part = text[midpoint:]
            half_duration = duration / 2

            # 添加前半部分
            subtitles.append({"text": first_part, "start": start, "duration": half_duration})

            # 添加后半部分，起始时间为之前的起始时间 + 半个时长
            subtitles.append({"text": second_part, "start": start + half_duration, "duration": half_duration})
        else:
            subtitles.append({"text": text, "start": start, "duration": duration})

    return subtitles
