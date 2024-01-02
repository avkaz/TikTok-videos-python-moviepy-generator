import requests
from api_request import ApiRequest
import json


class VideoScraper:
    def __init__(self):
        # Create an instance of ApiRequest
        self.api = ApiRequest()
        self.video_data = []  # Store video data for later use

    def fetch_data(self):
        # Get the URL, headers, and querystring from the ApiRequest instance
        url = self.api.url
        headers = self.api.get_headers()
        querystring = self.api.get_querystring()

        # Use the requests.get method to simplify the code
        response = requests.get(url, headers=headers, params=querystring)

        return response

    def process_data(self, response):
        # Check if the request was successful (status code 200)
        querystring = self.api.get_querystring().get('query', '')

        if response.status_code == 200:
            try:
                data = json.loads(response.text)
                videos = data.get('data', [])

                for video in videos:
                    attributes = video.get('attributes', {})
                    video_files = attributes.get('video', {}).get('video_files', [])

                    for file in video_files:
                        if file.get('quality') == 'hd' and int(file.get('width', 0)) <= 1000:
                            video_entry = {
                                'category': querystring,
                                'link': file.get('link'),
                                'used': 0
                            }
                            # Check if link already exists before appending
                            if video_entry['link'] not in [v['link'] for v in self.video_data]:
                                self.video_data.append(video_entry)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    def save_to_json(self, filename='../videos.json'):
        if self.video_data:
            # Check if link already exists in the file
            existing_links = set()
            try:
                with open(filename, 'r') as json_file:
                    existing_data = json.load(json_file)
                    existing_links = set(entry['link'] for entry in existing_data)
            except FileNotFoundError:
                pass  # File doesn't exist yet, which is fine

            # Only append new entries to the file
            new_entries = [entry for entry in self.video_data if entry['link'] not in existing_links]

            with open(filename, 'a') as json_file:
                json.dump(new_entries, json_file, indent=2)
            print(f"Data saved to {filename}")
        else:
            print("No video data available to save.")
