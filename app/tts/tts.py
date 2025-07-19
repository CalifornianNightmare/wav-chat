import torch
from os import environ

model = None


def load_tts():
    global model

    language = "ru"
    model_id = "v4_ru"
    device = torch.device(environ["DEVICE"])

    tts, _ = torch.hub.load(
        repo_or_dir="snakers4/silero-models",
        model="silero_tts",
        language=language,
        speaker=model_id,
    )
    tts.to(device)

    model = tts


def run_tts(text, sample_rate=48000, speaker="xenia", put_accent=True, put_yo=True):

    wav_path = model.save_wav(
        text=text,
        speaker=speaker,
        sample_rate=sample_rate,
        put_accent=put_accent,
        put_yo=put_yo,
        audio_path="files/output.wav",
    )

    return wav_path
