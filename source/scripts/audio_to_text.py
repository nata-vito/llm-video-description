import whisper

def speech_to_text(audio_file = "../audio/transcription.mp3", verbose = True):
    with open("../output/transcription.txt", "w") as file:
        model = whisper.load_model("medium")
        result = model.transcribe(audio_file)
        file.write(result["text"])
        
        if verbose:
            print(result["text"])


if __name__ == '__main__':
    speech_to_text()