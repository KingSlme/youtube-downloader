from pytube import YouTube
import os 

def download_mp4(url):
    try:
        youtube = YouTube(url)
        video_stream = youtube.streams.get_highest_resolution()
        target_file = f"{youtube.title}.mp4"
        counter = 1
        while os.path.exists(target_file):
            target_file = f"{youtube.title} ({counter}).mp4"
            counter += 1
        video_stream.download(filename=target_file)
        print("Video Download Complete")
    except Exception as e:
        print(f"Error {e}")

def download_mp3(url):
    try:
        youtube = YouTube(url)
        audio_stream = youtube.streams.filter(only_audio=True).first()
        target_file = f"{youtube.title}.mp3"
        counter = 1
        while os.path.exists(target_file):
            target_file = f"{youtube.title} ({counter}).mp3"
            counter += 1
        audio_stream.download(filename=target_file)
        print("Audio Download Complete")
    except Exception as e:
        print(f"Error {e}")