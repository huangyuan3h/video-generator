from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, TextClip, ImageClip, CompositeVideoClip

from task.utils import get_font_path


def merge_videos_with_background_music_and_overlays(video_paths, music_path, narration_path, output_path,
                                                    subtitles=None,
                                                    intro_image_path=None):
    """
    Merges videos with background music, narration, intro image, and optional subtitles from an SRT file.

    Args:
        video_paths (list of str): List of paths to the video files to merge.
        music_path (str): Path to the background music file.
        narration_path (str): Path to the narration audio file.
        output_path (str): Path to save the final video.
        srt_path (str): Path to the SRT subtitle file.
        intro_image_path (str): Path to an intro image that appears at the beginning.
    """
    try:
        # Step 1: 加载视频片段并去除原始音频
        clips = [VideoFileClip(path).without_audio() for path in video_paths]

        # Step 2: 合并视频片段
        main_video = concatenate_videoclips(clips, method="compose")

        # Step 3: 加载旁白音频，调整音量并设置视频时长
        narration = AudioFileClip(narration_path).volumex(1.5)
        final_duration = narration.duration + 2  # 旁白时长 + 2秒
        main_video = main_video.set_duration(final_duration)

        # Step 4: 添加背景音乐，并设置其时长与最终视频一致
        background_music = AudioFileClip(music_path).volumex(0.2)
        background_music = background_music.set_duration(final_duration)

        # Step 5: 创建首页图片片段（显示0.2秒）
        if intro_image_path:
            intro_image = ImageClip(intro_image_path).set_duration(0.2)
            intro_image = intro_image.set_fps(main_video.fps)
            clips.insert(0, intro_image)  # 在视频列表的开头插入首页图片
            main_video = concatenate_videoclips(clips, method="compose")

        # Step 6: 添加字幕
        if subtitles:
            subtitle_clips = []
            for sub in subtitles:
                txt_clip = TextClip(sub['text'], fontsize=32, color='white', font=get_font_path('NotoSansSC-Bold.ttf'),
                                    stroke_color="#f1f1f1", stroke_width=0.5)

                txt_clip = txt_clip.set_position(('center', main_video.h - 64)).set_start(sub['start']).set_duration(
                    sub['duration'])

                subtitle_clips.append(txt_clip)

            # 将字幕合成到主视频上
            main_video = CompositeVideoClip([main_video] + subtitle_clips)

        # Step 7: 将背景音乐和旁白音频叠加，并作为视频的音频轨道
        combined_audio = CompositeAudioClip([background_music, narration.set_start(0)])
        main_video = main_video.set_audio(combined_audio)

        # Step 8: 输出视频
        main_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

        print(f"视频已成功合并并保存至: {output_path}")

    except Exception as e:
        print(f"合并视频时出错: {e}")
