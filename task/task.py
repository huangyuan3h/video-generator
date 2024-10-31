from nanoid import generate
import os

from task.utils import get_task_folder


def create_new_task() -> str:
    task_id = generate(size=10)
    folder_path = get_task_folder(task_id)
    try:
        os.makedirs(folder_path)
        print(f"文件夹创建成功: {folder_path}")
    except OSError as error:
        print(f"创建文件夹失败: {error}")

    return task_id
