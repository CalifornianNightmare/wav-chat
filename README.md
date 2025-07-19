# wav-chat

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)

## About <a name = "about"></a>
ML project combining ASR with LLM to create audio chatting experience

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

- Python 3.12.3
- Pip
- Ollama

### Installing

A step by step series of examples that tell you how to get a development env running.

Create project folder

```sh
mkdir wav-chat
```
```sh
cd wav-chat
```

Clone this repository

```sh
git clone https://github.com/CalifornianNightmare/wav-chat
```

Set up virtual enviroment and log in

```sh
python -m venv .venv
```
```sh
source .venv/bin/activate
```

Install requirements

```sh
pip install --no-cache-dir -r requirements.txt
```

Install the ollama model that will be used (Llama3.2:1b by default)

```sh
ollama pull llama3.2:1b
```

Run the app

```sh
python app.py
```

### Runing in Docker <a name = "deployment">

Build the image (replace __wav-chat__ with custom name if necessary)

```sh
docker build -t wav-chat .
```

Run the image

```sh
docker run -it wav-chat
```

Run the image in bash (For debugging purposes)

```sh
docker run -it --entrypoint /bin/bash wav-chat
```


## Usage <a name = "usage"></a>

> ### Select a WAV

Searches for a WAV, transforms it to text, returns an llm summary voiced by tts

The files are read from and saved to the `/files/` folder. Only `.wav` types are allowed

> ### Clean WAV noise

Selects a WAV file and uses noise cancellation. Currently a WIP

> ### About

Shows short info box about the app

> ### Exit

Exits the app