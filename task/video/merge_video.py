from task.utils import get_font_path
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip, CompositeAudioClip, \
    TextClip, ImageClip


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
        subtitles (list of dict): List of subtitle entries, each with 'text', 'start', and 'duration' fields.
        intro_image_path (str): Path to an intro image that appears at the beginning.
    """
    try:
        # Step 1: Load video clips and remove original audio
        clips = [VideoFileClip(path).without_audio() for path in video_paths]

        # Step 2: Concatenate video clips
        main_video = concatenate_videoclips(clips, method="compose")

        # Step 3: Load narration audio, adjust volume
        narration = AudioFileClip(narration_path).volumex(1.5)

        # Step 4: Load background music and set its volume
        background_music = AudioFileClip(music_path).volumex(0.2)

        # Step 5: Calculate final duration based on the shorter of narration or background music
        final_duration = min(narration.duration, background_music.duration)
        main_video = main_video.set_duration(final_duration)

        # Step 6: Create an intro image clip (displayed for 0.5 seconds)
        if intro_image_path:
            intro_image = ImageClip(intro_image_path).set_duration(0.5)
            intro_image = intro_image.set_fps(main_video.fps)
            clips.insert(0, intro_image)  # Insert intro image at the beginning of the clip list
            main_video = concatenate_videoclips(clips, method="compose")

        # Step 7: Add subtitles
        if subtitles:
            subtitle_clips = []
            is_portrait = main_video.h > main_video.w  # Check if the video is in portrait mode
            for sub in subtitles:
                txt_clip = TextClip(sub['text'], fontsize=32, color='white', font=get_font_path('NotoSansSC-Bold.ttf'),
                                    stroke_color="#f1f1f1", stroke_width=1)

                # Set subtitle position based on orientation
                if is_portrait:
                    subtitle_position = ('center', int(main_video.h * 0.75))  # Center and move up slightly for portrait
                else:
                    subtitle_position = ('center', main_video.h - 64)  # Position near the bottom for landscape

                txt_clip = txt_clip.set_position(subtitle_position).set_start(sub['start']).set_duration(sub['duration'])
                subtitle_clips.append(txt_clip)

            # Overlay subtitles on the main video
            main_video = CompositeVideoClip([main_video] + subtitle_clips)

        # Step 8: Combine background music and narration as the audio track for the video
        combined_audio = CompositeAudioClip([background_music.set_duration(final_duration), narration.set_duration(final_duration)])
        main_video = main_video.set_audio(combined_audio)

        # Step 9: Force the final video duration to match the audio
        main_video = main_video.set_duration(final_duration)

        # Step 10: Export the final video
        main_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

        print(f"Video successfully merged and saved to: {output_path}")

    except Exception as e:
        print(f"Error during video merging: {e}")
