FROM python:3.12.3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt update
RUN apt install ffmpeg --yes

COPY . .

VOLUME ./files /usr/src/app/files
wwww
ENV TERM=xterm-256color

SHELL ["/bin/bash", "-c"]
RUN python ./app.py