import whisper

def speech_to_text(audio_file = "./source/audio/transcription.mp3", verbose = True):
    with open("./source/output/transcription.txt", "w") as file:
        model = whisper.load_model("medium")
        result = model.transcribe(audio_file)
        file.write(result["text"])
        
        if verbose:
            print("Text transcription", result["text"])


if __name__ == '__main__':
    speech_to_text()