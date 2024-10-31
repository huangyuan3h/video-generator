import os

import edge_tts

from task.utils import get_audio_path


async def text_to_speech(text: str, voice: str, task_id):
    """
    将文本转换成语音，并保存到指定路径。

    Args:
        text (str): 要转换的文本内容。
        voice (str): 语音的类型，例如 'zh-CN-XiaoxiaoNeural'。
        task_id (str):
    """
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(get_audio_path(task_id))
