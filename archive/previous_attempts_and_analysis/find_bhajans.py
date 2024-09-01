import argparse
import librosa
import numpy as np

def find_bhajan_starts(audio_file, threshold):
    # Load the audio file
    audio_data, sampling_rate = librosa.load(audio_file)

    # Compute the amplitude (RMS value)
    rms = librosa.feature.rms(y=audio_data)[0]

    # Define duration of each frame (default hop length = 512)
    frame_duration = 512 / sampling_rate

    # Find potential bhajan starts
    bhajan_starts = []
    below_threshold = True
    for i in range(len(rms)):
        # If current amplitude is above threshold and previous frames were below threshold
        if rms[i] > threshold and below_threshold:
            start = i * frame_duration
            bhajan_starts.append(start)
            below_threshold = False
        elif rms[i] <= threshold:
            below_threshold = True

    return bhajan_starts

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find potential start times of bhajans in an audio file.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the audio file')

    args = parser.parse_args()

    threshold = 0.05  # Amplitude threshold for detecting bhajan starts

    bhajan_starts = find_bhajan_starts(args.file, threshold)

    print("Potential bhajan start times:")
    for start_time in bhajan_starts:
        start_min, start_sec = divmod(start_time, 60)
        print(f"{int(start_min)}:{start_sec:.2f}")