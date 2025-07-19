FROM python:3.12.3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN curl -fsSL https://ollama.com/install.sh | sh
RUN ollama pull llama3.2:1b

COPY . .

VOLUME ./files /usr/src/app/files

ENTRYPOINT ["/bin/bash", "-c", "python ./app.py"]