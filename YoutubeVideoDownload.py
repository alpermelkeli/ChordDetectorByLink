import os
import sys

from pytube import YouTube


def turkish_to_english(text):
    letters = {"ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u"}
    translated_text = ""

    for char in text:
        if char.lower() in letters:
            if char.isupper():
                translated_text += letters[char.lower()].upper()
            else:
                translated_text += letters[char.lower()]
        else:
            translated_text += char

    return translated_text





def download_video(url, output_path='C:/Users/alper/OneDrive/Masaüstü/autochordapp'):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Download the video
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    video_title = yt.title
    video_title = video_title.lower()
    video_title = turkish_to_english(video_title)
    video_stream.download(output_path, filename=video_title+".mp4")

    print(f"Video '{video_title}' downloaded successfully!")

if __name__ == "__main__":
    # Enter the YouTube video URL
    video_url = sys.argv[1]
    download_video(video_url)



