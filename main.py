import asyncio

from task.subtitle import generate_srt_by_task_id
from task.task import create_new_task
from task.tts import text_to_speech

text_content = "Hello, this is a test. we need to generate some text here."
voice_option = "en-CA-LiamNeural"





taskId = create_new_task()
print(taskId)
asyncio.run(text_to_speech(text_content,voice_option, taskId))
generate_srt_by_task_id(taskId)


