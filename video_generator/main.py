from config import *
from generator import VideoGenerator

video_maker = VideoGenerator()



x = 0
while x < 10:
    video_path = download_video_from_json('../videos.json', 'walking')
    audio_path = load_audio_path_from_folder('../audio')
    text_path = load_text_from_json('../quotes.json')
    resulting_video = video_maker.generate(video_path, audio_path, text_path)
    print(f"Video created: {resulting_video}")
    x += 1





