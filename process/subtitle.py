import whisper
import edge_tts
import tempfile


def text_to_voice(text, voice="en-CA-LiamNeural"):
    return edge_tts.Communicate(text, voice)


def load_audio_bytes(audio_bytes):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_mp3:
        temp_mp3.write(audio_bytes)
        temp_mp3.flush()

        return whisper.load_audio(temp_mp3.name)


def transcribe_audio_by_path(audio_path, model_name="base"):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result


def transcribe_audio_from_bytes(audio_bytes, model_name="base"):
    model = whisper.load_model(model_name)

    audio = load_audio_bytes(audio_bytes)

    result = model.transcribe(audio)
    return result


def generate_srt(transcribed):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".srt") as temp_srt:
        for item in transcribed["segments"]:
            temp_srt.write(f"{item['id'] + 1}\n".encode("utf-8"))
            temp_srt.write(f"{item['start']} --> {item['end']}\n".encode("utf-8"))
            temp_srt.write(f"{item['text']}\n\n".encode("utf-8"))

        return temp_srt.name
