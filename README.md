# Auto Video Description

Tool to help video description generation for multi purposes.

## How to Install:

```bash
# Clone repository
git clone <repository-url>
cd llm-video-description

# Install the dependencies
sudo apt update && sudo apt install ffmpeg
pip install -r requirements.txt

# ollama serve
curl -fsSL https://ollama.com/install.sh | sh

# Install llama3.1 
ollama pull llama3.1

# Run llama3.1
ollama serve

# Run the script
python source/scripts/audio_to_text.py
```

## How to Use:
- 1 - Create the folder llm-video-description/source/audio/, llm-video-description/source/output/ and import your audio file to this new path
- 1.1 - Change the audio file name to transcription.mp3
- 2 - Run the commands in the root folder:

```bash
# Run the script
python source/scripts/audio_to_text.py
```

## How to fix it:

To:
```bash
bind: address already in use
```

Do:
```bash
systemctl stop ollama
ollama serve
```

## TODO:
- LMM Speech to text: DONE
- LLM to generate description: DONE
- Easy to use: ---