# Facebook-reels-donwloader
download Facebook reels by giving reels URLs
This Python script is designed to download videos from a list of URLs using the yt-dlp library and store them in a specified directory. It prompts the user to input video URLs one by one until they decide to finish. After downloading all the videos, it asks the user if they want to exit the program.

Here's a breakdown of how the script works:

The download_video function takes a video URL and an output directory as input. It constructs a command to download the video using yt-dlp with the specified format and output directory. Then, it runs the command as a subprocess and prints the output and errors.

The main function contains the main logic of the script. It continuously prompts the user to enter video URLs until they decide to finish by entering 'd'. After collecting all the URLs, it downloads each video using the download_video function.

It asks the user if they want to exit the program. If the user chooses to exit by entering 'y', the script terminates.

To use this script, you need to have yt-dlp installed and accessible from the command line.

If you have any specific questions or need further assistance with this script, feel free to ask!
