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