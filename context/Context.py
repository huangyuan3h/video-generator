from dataclasses import dataclass


@dataclass
class VideoParameter:
    content: str = ""  # that the content you find from some website (required)
    language: str = "Chinese"  # language (required)
    title: str = None  # default to none
    scripts: str = None  # speech that generated to video
    taskId: str = None
    voice_option: str = "zh-CN-YunxiNeural"  # voice sound
    background_music: str = "resources/background_music/Owls.mp3"
    video_orientations = ["landscape", "portrait"]
    qr_url: str = None
