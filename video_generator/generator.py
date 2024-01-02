import os
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip

class VideoGenerator:
    def generate(self, video_path, audio_path, text, output_folder='../output_videos', target_duration=7):
        try:
            # Ensure the output folder exists
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Load video and audio clips
            video_clip = VideoFileClip(video_path)

            # Set video duration to the target duration (in seconds)
            video_clip = video_clip.subclip(0, target_duration)

            audio_clip = AudioFileClip(audio_path).subclip(0, target_duration)

            # Set video audio and trim audio
            video_clip = video_clip.set_audio(audio_clip)

            # Calculate fontsize based on the smaller dimension of the video
            fontsize_percentage = 7
            fontsize = int(min(video_clip.size) * fontsize_percentage / 100)

            # Calculate the height offset to position the text a little higher than the center
            height_offset = int(video_clip.size[1] * 0.35)

            # Split the text into lines
            lines = text.split('\n')

            # Create TextClips for each line
            text_clips = []
            for line in lines:
                text_clip = TextClip(line, fontsize=fontsize, color='white', bg_color='black',
                                     font='BebasNeue-Regular', size=(video_clip.size[0] // 1, None),
                                     method='caption', align='center', interline=-10)
                text_clip = text_clip.set_duration(video_clip.duration).set_position(('center', height_offset))
                text_clips.append(text_clip)

            # Stack TextClips vertically
            text_clip = CompositeVideoClip(text_clips, size=video_clip.size).set_opacity(0.8)

            # Composite video clip with text
            final_clip = CompositeVideoClip([video_clip, text_clip])

            # Generate a more descriptive output filename
            output_filename = self.get_output_filename(output_folder)

            # Write the final video with audio and text
            final_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac",
                                       temp_audiofile="temp-audio.m4a", remove_temp=True)

            return output_filename

        except Exception as e:
            print(f"Error generating video: {e}")
            return None

    def get_output_filename(self, output_folder):
        counter = 1
        output_filename = f"{output_folder}/output_video_{counter}.mp4"
        while os.path.exists(output_filename):
            counter += 1
            output_filename = f"{output_folder}/output_video_{counter}.mp4"
        return output_filename
