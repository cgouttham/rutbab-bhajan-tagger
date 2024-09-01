import argparse
import librosa
import numpy as np

def find_amplitude_at_time(audio_file, time):
    # Load the audio file
    audio_data, sampling_rate = librosa.load(audio_file)

    # Compute the amplitude (RMS value)
    rms = librosa.feature.rms(y=audio_data)[0]

    # Define duration of each frame (default hop length = 512)
    frame_duration = 512 / sampling_rate

    # Convert time to frame index
    frame_index = int(time / frame_duration)

    # Get amplitude at the specific frame
    amplitude = rms[frame_index]

    return amplitude

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find amplitude at a specific time in an audio file.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the audio file')
    parser.add_argument('-t', '--time', type=float, required=True, help='Time (in seconds) at which to find the amplitude')

    args = parser.parse_args()

    amplitude = find_amplitude_at_time(args.file, args.time)

    print(f"Amplitude at time {args.time} seconds: {amplitude}")