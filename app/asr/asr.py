import whisper

model = None


def load_asr():
    global model
    model = whisper.load_model("small")


def run_asr(filename="files/input.wav"):
    result = model.transcribe(filename, fp16=False)
    return result["text"]
