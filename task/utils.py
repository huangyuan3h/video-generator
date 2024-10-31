import os


def get_task_folder(task_id: str) -> str:
    base_dir = "tasks"

    folder_path = os.path.join(base_dir, task_id)
    return folder_path


def get_audio_path(task_id: str) -> str:
    return os.path.join(get_task_folder(task_id), 'audio.mp3')

def get_srt_path(task_id: str) -> str:
    return os.path.join(get_task_folder(task_id), 'subtitle.srt')
