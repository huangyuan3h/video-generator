import asyncio
import tempfile

from process.subtitle import text_to_voice, transcribe_audio_from_bytes, generate_srt

text_content = "Hello, this is a test. we need to generate some text here."
voice_option = "en-CA-LiamNeural"


async def generate_subtitle():
    communicate = text_to_voice(text_content, voice_option)

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        await communicate.save(temp_file.name)

        temp_file.seek(0)
        audio_bytes = temp_file.read()
        transcribed = transcribe_audio_from_bytes(audio_bytes)
        srt = generate_srt(transcribed)


asyncio.run(generate_subtitle())
