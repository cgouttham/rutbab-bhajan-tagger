import argparse
import librosa
import numpy as np
from datetime import timedelta
from rich import print
from rich.table import Table
from yt_dlp import YoutubeDL
from tqdm import tqdm
from urllib.parse import urlparse, parse_qs
import os

class TqdmUpTo(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def extract_video_id_from_url(url):
    """
    Parses URL and returns YouTube Video ID
    """
    parsed_url = urlparse(url)
    if parsed_url.query:
        parsed_query_string = parse_qs(parsed_url.query)
        if "v" in parsed_query_string:
            return parsed_query_string["v"][0]
    elif parsed_url.path:
        path_parts = parsed_url.path.split("/")
        if path_parts and path_parts[1]:
            return path_parts[1]
    return None

def download_audio_from_youtube(video_id, output_folder="."):
    def my_hook(d):
        if d['status'] == 'finished':
            print('\nDone downloading, now converting ...')
        elif d['status'] == 'downloading':
            print(f"Downloading... {d['_percent_str']}", end='\r')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/{video_id}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'prefer_ffmpeg': True,
        'progress_hooks': [my_hook],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'http://www.youtube.com/watch?v={video_id}'])
               
def analyze_audio(audio_file, min_duration, percentile, time_diff):
    # Load the audio file
    audio_data, sampling_rate = librosa.load(audio_file)

    # Compute the amplitude (RMS value)
    rms = librosa.feature.rms(y=audio_data)[0]

    # Define duration of each frame (default hop length = 512)
    frame_duration = 512 / sampling_rate

    # Compute percentiles
    percentiles = [1, 5, 10, 25, 50, 75, 90, 95, 100]
    percentile_values = [np.percentile(rms, p) for p in percentiles]

    # Use the specified percentile as the threshold for silence
    silence_threshold = np.percentile(rms, percentile)

    # Find moments of silence lasting at least min_duration
    silence_starts = []
    start = None
    for i in range(len(rms)):
        if rms[i] <= silence_threshold and start is None:
            start = i * frame_duration
        elif rms[i] > silence_threshold and start is not None:
            end = i * frame_duration
            if end - start >= min_duration:
                silence_starts.append(start)
            start = None

    # Filter start times that are within the specified time difference of each other
    final_starts = []
    for i in range(len(silence_starts)):
        if i == 0 or silence_starts[i] - silence_starts[i - 1] >= time_diff:
            final_starts.append(silence_starts[i])

    return percentile_values, final_starts

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze an audio file and find potential start times of bhajans.')
    parser.add_argument('-f', '--file', type=str, help='Path to the audio file')
    parser.add_argument('-y', '--youtube', type=str, help='YouTube video ID or URL to analyze')
    parser.add_argument('--from-youtube', action='store_true', help='Download the audio file from YouTube before analyzing')
    parser.add_argument('-d', '--duration', type=float, default=2.0, help='Minimum duration of silence between bhajans in seconds')
    parser.add_argument('-p', '--percentile', type=int, default=15, help='Percentile to use as the threshold for silence')
    parser.add_argument('-t', '--time_diff', type=float, default=60.0, help='Minimum time difference between start times in seconds')
    parser.add_argument('-pp', '--pretty_print', action='store_true', default=True, help='Print start times with "Bhajan X: " prefix')

    args = parser.parse_args()

    print(f"[bold cyan]Running audio analysis with the following parameters:[/bold cyan]")
    print(f"Audio file: {args.file}")
    print(f"Minimum duration of silence between bhajans: {args.duration} seconds")
    print(f"Percentile to use as the threshold for silence: {args.percentile}%")
    print(f"Minimum time difference between start times: {args.time_diff} seconds")
    print(f"Pretty print start times: {'Yes' if args.pretty_print else 'No'}")
    print(f"YouTube video ID: {args.youtube if args.youtube else 'Not provided'}")

    if not args.from_youtube and not args.file:
        raise ValueError("You must provide either a local file with --file or a YouTube video ID with --from-youtube and --youtube")

    if args.from_youtube:
        output_folder = "assets/youtube_downloads"
        os.makedirs(output_folder, exist_ok=True)   # create directory if it does not exist
        video_id = extract_video_id_from_url(args.youtube)
        if video_id is None:
            raise ValueError("Invalid YouTube URL or video ID")
        print(f"[bold cyan]Downloading audio from YouTube video ID: {video_id}[/bold cyan]")
        download_audio_from_youtube(video_id, output_folder=output_folder)
        args.file = f"{output_folder}/{video_id}.mp3"

    percentile_values, silence_starts = analyze_audio(args.file, args.duration, args.percentile, args.time_diff)

    # Create a table for the percentiles
    percentile_table = Table(title="Amplitude Percentiles")
    percentile_table.add_column("Percentile", style="cyan")
    percentile_table.add_column("Value", style="magenta")
    percentiles = [5, 15, 85, 95]
    for p, v in zip(percentiles, percentile_values):
        percentile_table.add_row(f"{p}%", f"{v:.5f}")

    print(percentile_table)

    # Print the percentile being used for the silence threshold
    print(f"[bold cyan]Using the {args.percentile}% percentile as the threshold for silence[/bold cyan]")

    # Print the start times
    print("[bold cyan]Potential bhajan start times:[/bold cyan]")
    for i, start_time in enumerate(silence_starts, 1):
        start_time_seconds = int(start_time)
        start_time = timedelta(seconds=start_time_seconds)
        if args.pretty_print:
            print(f"[green]Bhajan {i}: {str(start_time)}[/green]")
        else:
            print(f"[green]{str(start_time)}[/green]")

        # If the YouTube flag is present, print the YouTube URL
        if args.youtube:
            youtube_link = f"https://www.youtube.com/watch?v={video_id}&t={start_time_seconds}s"
            print(f"[blue]{youtube_link}[/blue]")