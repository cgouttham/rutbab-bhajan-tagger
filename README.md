# Sai Bhajan Tagger

This project is an audio analyzer to find potential start times of bhajans in an audio file.

## Setup

Follow these steps to setup the project.

1. Clone the repository:

```bash
git clone https://github.com/your-username/sai-bhajan-tagger.git
cd sai-bhajan-tagger
```

2. Set up a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The script takes an audio file as input and outputs potential start times of bhajans based on moments of silence in the audio. It uses RMS value to calculate the amplitude of the audio and uses a percentile of this amplitude as the threshold for silence.

Here is how to run the script:

```bash
python find_bhajans.py -f /path/to/audio/file
```

Another example
```bash
# Input:
python rushis_post_bhajan_minion.py --from-youtube --youtube https://www.youtube.com/watch\?app\=desktop\&v\=h-rz0o9ew6U

# Sample output
Audio file: None
Minimum duration of silence between bhajans: 2.0 seconds
Percentile to use as the threshold for silence: 15%
Minimum time difference between start times: 60.0 seconds
Pretty print start times: Yes
YouTube video ID: https://www.youtube.com/watch?app=desktop&v=h-rz0o9ew6U
Downloading audio from YouTube video ID: h-rz0o9ew6U
[youtube] Extracting URL: http://www.youtube.com/watch?v=h-rz0o9ew6U
[youtube] h-rz0o9ew6U: Downloading webpage
[youtube] h-rz0o9ew6U: Downloading ios player API JSON
[youtube] h-rz0o9ew6U: Downloading web creator player API JSON
[youtube] h-rz0o9ew6U: Downloading m3u8 information
[info] h-rz0o9ew6U: Downloading 1 format(s): 251
[download] Destination: assets/youtube_downloads/h-rz0o9ew6U.webm
[download] 100% of   51.32MiB in 00:00:10 at 4.96MiB/s
Done downloading, now converting ...

[ExtractAudio] Destination: assets/youtube_downloads/h-rz0o9ew6U.mp3
Deleting original file assets/youtube_downloads/h-rz0o9ew6U.webm (pass -k to keep)
 Amplitude Percentiles
┏━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Percentile ┃ Value   ┃
┡━━━━━━━━━━━━╇━━━━━━━━━┩
│ 5%         │ 0.01253 │
│ 15%        │ 0.03243 │
│ 85%        │ 0.05694 │
│ 95%        │ 0.09346 │
└────────────┴─────────┘
Using the 15% percentile as the threshold for silence
Potential bhajan start times:
Bhajan 1: 0:00:00
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=0s
Bhajan 2: 0:03:29
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=209s
Bhajan 3: 0:09:56
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=596s
Bhajan 4: 0:15:02
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=902s
Bhajan 5: 0:19:08
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=1148s
Bhajan 6: 0:24:09
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=1449s
Bhajan 7: 0:26:23
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=1583s
Bhajan 8: 0:28:33
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=1713s
Bhajan 9: 0:32:07
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=1927s
Bhajan 10: 0:34:16
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=2056s
Bhajan 11: 0:39:40
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=2380s
Bhajan 12: 0:44:54
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=2694s
Bhajan 13: 0:49:19
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=2959s
Bhajan 14: 0:53:28
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=3208s
Bhajan 15: 0:57:46
https://www.youtube.com/watch?v=h-rz0o9ew6U&t=3466s
```

### Available Arguments

Here are the arguments that can be provided to the script:

- `-f`, `--file` (required): Path to the audio file.
- `-d`, `--duration` (optional): Minimum duration of silence between bhajans in seconds. Default is 2.0.
- `-p`, `--percentile` (optional): Percentile to use as the threshold for silence. Default is 15.
- `-t`, `--time_diff` (optional): Minimum time difference between start times in seconds. Default is 60.0.
- `-pp`, `--pretty_print` (optional): If provided, print start times with "Bhajan X: " prefix.
- `-yt`, `--youtube` (optional): YouTube video ID to generate URLs for each start time.

## Contribution

Contributions are always welcome! Please feel free to submit a pull request.