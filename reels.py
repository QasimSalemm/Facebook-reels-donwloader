import subprocess
import sys
import os

def download_video(video_url, output_dir):
    # Download the video using yt-dlp
    args = ["yt-dlp", "-f", "b", "-o", f"{output_dir}/%(id)s.%(ext)s", video_url]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Print output and errors
    while True:
        output = process.stdout.readline()
        error = process.stderr.readline()
        if output == '' and error == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
        if error:
            print(error.strip(), file=sys.stderr)

def main():
    while True:
        output_dir = "Facebook_Reels"
        os.makedirs(output_dir, exist_ok=True)

        urls = []  # List to store URLs

        # Prompt the user to enter video URLs
        while True:
            video_url = input("Enter video URL one by one (Enter 'd' to finish): ")
            if video_url.lower() == 'd':
                break
            urls.append(video_url)

        # Download videos for each URL
        for video_url in urls:
            download_video(video_url, output_dir)

        # Ask the user if they want to exit
        choice = input("Do you want to exit? (y/n): ")
        if choice.lower() == 'y':
            break

if __name__ == "__main__":
    main()
