FROM python:3.12.3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt update
RUN apt install ffmpeg --yes

COPY . .

VOLUME ./files /usr/src/app/files

CMD ["python", "./app.py"]