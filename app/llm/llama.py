# This assumes you've already pulled the model via ollama

import ollama
from os import environ


def run_llama(text):
    prompt = f"Сгенерируй краткий осмысленный ответ на русском языке: {text}"

    result = ollama.generate(model=environ['LLM_MODEL_VERSION'], prompt=prompt)

    return result["response"]
