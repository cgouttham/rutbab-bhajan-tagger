import argparse
import librosa
import numpy as np

def analyze_audio(audio_file, top_n):
    # Load the audio file
    audio_data, sampling_rate = librosa.load(audio_file)

    # Compute the amplitude (RMS value)
    rms = librosa.feature.rms(y=audio_data)[0]

    # Define duration of each frame (default hop length = 512)
    frame_duration = 512 / sampling_rate

    # Define the threshold
    threshold = 0.025

    # Find intervals with low amplitude
    intervals = []
    start = None
    for i in range(len(rms)):
        # Start of a low amplitude interval
        if rms[i] < threshold and start is None:
            start = i * frame_duration
        # End of a low amplitude interval
        elif rms[i] >= threshold and start is not None:
            end = i * frame_duration
            intervals.append((start, end))
            start = None

    # If the last frame was also below the threshold, close the interval
    if start is not None:
        end = len(rms) * frame_duration
        intervals.append((start, end))

    # Sort the intervals by their length in descending order
    intervals.sort(key=lambda interval: interval[1] - interval[0], reverse=True)

    # Get the top N intervals
    top_intervals = intervals[:top_n]

    # Sort the top N intervals by start time
    top_intervals.sort(key=lambda interval: interval[0])

    # Print the top N intervals
    for interval in top_intervals:
        start_min, start_sec = divmod(interval[0], 60)
        end_min, end_sec = divmod(interval[1], 60)
        duration = interval[1] - interval[0]
        print(f"Start: {int(start_min)}:{start_sec:.2f}, End: {int(end_min)}:{end_sec:.2f}, Duration: {duration:.2f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze audio file for intervals of low amplitude.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the audio file')
    parser.add_argument('-n', '--num_intervals', type=int, required=True, help='Number of top intervals to print')

    args = parser.parse_args()

    analyze_audio(args.file, args.num_intervals)