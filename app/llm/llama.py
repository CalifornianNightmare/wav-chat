# This assumes you've already pulled the model via ollama

import ollama


def run_llama(text):
    prompt = f"Сгенерируй краткий осмысленный ответ на русском языке: {text}"

    result = ollama.generate(model="llama3.2:1b", prompt=prompt)

    return result["response"]
