from dotenv import load_dotenv
from os import environ

from app.menu import main_menu


def load_models():

    from app.asr.asr import load_asr
    from app.tts.tts import load_tts

    load_asr()
    print("ASR model loaded") if int(environ["VERB"]) >= 2 else None
    load_tts()
    print("TTS model loaded") if int(environ["VERB"]) >= 2 else None


if __name__ == "__main__":
    load_dotenv()
    load_models()

    main_menu()
