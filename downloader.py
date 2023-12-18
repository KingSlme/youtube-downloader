import os
import re
from pytube import YouTube
from pytube.exceptions import *
import ffmpeg

def handle_errors(e):
    error_messages = {
        RegexMatchError: "Invalid URL",
        AgeRestrictedError: "Age restricted",
        VideoPrivate: "Video private",
        VideoRegionBlocked: "Video region blocked",
        RecordingUnavailable: "Recording unavailable",
        MembersOnly: "Video is members only",
        LiveStreamError: "Video is a live stream",
        VideoUnavailable: "Video unavailable",
        MaxRetriesExceeded: "Maximum retries exceeded",
        ExtractError: "Data extraction failed",
        HTMLParseError: "HTML parsing failed",
        FileNotFoundError: "FFmpeg missing, check README"
    }
    return f"Error: {error_messages.get(type(e), str(e))}"

def download_video(url, callback, file_extension):
    try:
        youtube = YouTube(url, on_progress_callback=callback)
        video_stream = None
        if file_extension == "mp4":
            video_stream = youtube.streams.get_highest_resolution()
        elif file_extension == "mp3":
            video_stream = youtube.streams.filter(only_audio=True).first()
        if not video_stream:
            return "Error: Video stream not available"
        youtube_title = re.sub(r'[\\/:*?"<>|]', '', youtube.title).rstrip('.')
        target_file = f"{youtube_title}.mp4"
        counter = 1
        while os.path.exists(target_file):
            target_file = f"{youtube_title} ({counter}).mp4"
            counter += 1
        video_stream.download(filename=target_file)
        if file_extension == "mp3":
            convert_mp4_to_mp3(target_file, youtube_title)
        return "Download Completed!"
    except Exception as e:
        return handle_errors(e)

def convert_mp4_to_mp3(input_file, youtube_title):
    output_file = f"{youtube_title}.mp3"
    counter = 1
    while os.path.exists(output_file):
        output_file = f"{youtube_title} ({counter}).mp3"
        counter += 1
    ffmpeg.input(input_file).output(output_file, acodec='libmp3lame', q=2).run(overwrite_output=True)
    print(f"Conversion successful: {input_file} converted to {output_file}")
    os.remove(input_file)