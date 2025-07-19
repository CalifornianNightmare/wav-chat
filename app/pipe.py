from app.asr.asr import run_asr
from app.llm.llama import run_llama
from app.tts.tts import run_tts

from os import environ


def pipeline(input_file):
    print(f"Reading audio file...\n\n") if int(environ["VERB"]) >= 1 else None
    wavtext = run_asr(input_file)
    print(f"Wav text: {wavtext}\n\n") if int(environ["VERB"]) >= 1 else None
    print(f"Generating reply text...") if int(environ["VERB"]) >= 1 else None
    reply_text = run_llama(wavtext)
    print(f"Reply text: {reply_text}\n\n") if int(environ["VERB"]) >= 1 else None
    print(f"Running TTS...") if int(environ["VERB"]) >= 1 else None
    reply_audio_path = run_tts(reply_text)
    return reply_audio_path
