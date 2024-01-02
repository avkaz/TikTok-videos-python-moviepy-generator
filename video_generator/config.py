import json
import requests
import os
import random


def download_video_from_json(json_path, category, output_path='downloaded_video.mp4'):
    try:
        # Load the JSON file from the local file system
        with open(json_path, 'r') as file:
            json_data = json.load(file)

        # Find the first video with the specified category and unused status
        video_to_download = None
        for video in json_data:
            if video.get('category') == category and video.get('used', 0) == 0 and video.get('link'):
                video_to_download = video
                break

        if video_to_download:
            # Download the video
            video_url = video_to_download['link']
            video_response = requests.get(video_url, stream=True)
            with open(output_path, 'wb') as file:
                for chunk in video_response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)

            print(f"Video downloaded successfully to: {output_path}")

            # Set the "used" value to 1
            video_to_download['used'] = 1

            # Update the local JSON file with the modified data
            with open(json_path, 'w') as json_file:
                json.dump(json_data, json_file, indent=2)

            return output_path
        else:
            print(f"No available video found for category '{category}'")
            return None

    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

def load_text_from_json(json_path):
    try:
        # Load the JSON file from the local file system with specified encoding
        with open(json_path, 'r', encoding='latin-1') as file:
            json_data = json.load(file)

        # Find the first text with unused status
        text_to_return = None
        for text_entry in json_data:
            if text_entry.get('used', 0) == 0 and 'text' in text_entry:
                text_to_return = text_entry['text']
                # Set the "used" value to 1
                text_entry['used'] = 1
                break

        if text_to_return:
            # Update the local JSON file with the modified data
            with open(json_path, 'w', encoding='latin-1') as json_file:
                json.dump(json_data, json_file, indent=2, ensure_ascii=False)

            return text_to_return
        else:
            print("No available unused text found.")
            return None

    except Exception as e:
        print(f"Error loading text from JSON: {e}")
        return None



def load_audio_path_from_folder(folder_path):
    try:
        # Get a list of all audio files in the specified folder
        audio_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav', '.ogg'))]

        if not audio_files:
            print(f"No audio files found in the folder: {folder_path}")
            return None

        # Choose a random audio file
        random_audio_file = random.choice(audio_files)
        random_audio_path = os.path.join(folder_path, random_audio_file)

        print(f"Random audio path selected: {random_audio_path}")

        return random_audio_path

    except Exception as e:
        print(f"Error loading audio path from folder: {e}")
        return None