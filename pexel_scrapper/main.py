from scraper import VideoScraper  # Assuming the class is in video_scraper.py

def main():
    # Create an instance of VideoScraper
    video_scraper = VideoScraper()

    # Fetch data
    response = video_scraper.fetch_data()

    # Process data
    video_scraper.process_data(response)

    # Save data to CSV
    video_scraper.save_to_json()

if __name__ == "__main__":
    main()
