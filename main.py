import asyncio

from llm.llm_client import get_llm_client
from task.subtitle import generate_srt_by_task_id
from task.task import create_new_task
from task.tts import text_to_speech, get_mp3_duration

text_content = "Hello, this is a test. we need to generate some text here."
voice_option = "en-CA-LiamNeural"




# seconds = get_mp3_duration('XgCkyF-MGu')
# print(seconds)

# model = get_llm_client()
#
# response = model.generate_content(["hello"])
# print(response.text)


# taskId = create_new_task()
# print(taskId)
# asyncio.run(text_to_speech(text_content,voice_option, taskId))
# generate_srt_by_task_id(taskId)
