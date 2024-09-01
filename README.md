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
(env) ➜  sai-bhajan-tagger git:(main) ✗ python rushis_post_bhajan_minion.py -f assets/full_rutbab_blocks/block_f_all.mp3 -d 2.0 -pp -yt AX9fbmS5OdY

# Sample output
Running audio analysis with the following parameters:
Audio file: assets/full_rutbab_blocks/block_f_all.mp3
Minimum duration of silence between bhajans: 2.0 seconds
Percentile to use as the threshold for silence: 15%
Minimum time difference between start times: 60.0 seconds
Pretty print start times: Yes
YouTube video ID: AX9fbmS5OdY
Amplitude Percentiles

┏━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Percentile ┃ Value   ┃
┡━━━━━━━━━━━━╇━━━━━━━━━┩
│ 5%         │ 0.01219 │
│ 15%        │ 0.03195 │
│ 85%        │ 0.05398 │
│ 95%        │ 0.08536 │
└────────────┴─────────┘
Using the 15% percentile as the threshold for silence
Potential bhajan start times:
Bhajan 1: 0:00:00
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=0s
Bhajan 2: 0:03:33
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=213s
Bhajan 3: 0:07:48
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=468s
Bhajan 4: 0:15:01
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=901s
Bhajan 5: 0:18:43
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=1123s
Bhajan 6: 0:22:00
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=1320s
Bhajan 7: 0:27:06
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=1626s
Bhajan 8: 0:30:54
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=1854s
Bhajan 9: 0:35:06
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=2106s
Bhajan 10: 0:39:31
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=2371s
Bhajan 11: 0:44:52
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=2692s
Bhajan 12: 0:51:02
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=3062s
Bhajan 13: 0:55:20
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=3320s
Bhajan 14: 0:59:06
https://www.youtube.com/watch?v=AX9fbmS5OdY&t=3546s
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