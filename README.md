# RECCOMENDATION ASSISTANT

|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zytoYEWeo2HULtUaTkH5nKZJNk5SQgD8?usp=sharing)|

## Setup
Install Docker.

```sh
$ git clone https://github.com/VladimirKalajcidi/Recommendation-Assistant.git
$ cd Recommendation-Assistant
$ docker build -t llm .
```

## Usage
### Generating questions 
Execute following command in `Recommendation-Assistant` directory.

```sh
$ docker run -it -d -v $(pwd):/app/ --net host --name llm llm
$ docker exec -it llm bash
root@hostname:/workspace# ./scripts/installation.sh
root@hostname:/workspace# python main.py -i text
```
Arguments for `main.py`:
```sh
    - i: input text
```