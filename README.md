# NG's NLTLK Playground

This is a playground for me to learn and experiment with the Natural Language Toolkit (NLTK) in Python.

## Installation

To install the required packages, run the following command:

```bash
poetry install
```

## Usage

### Sentiment

To run the sentiment analysis, run the following command:

```bash
poetry run python ./ng_nltk_playground/sentiment.py --interactive
```

This will run in interactive mode, allowing you to enter text and get the results instantly.

You can also run the sentiment analysis on a file by running the following command:

```bash
poetry run python ./ng_nltk_playground/sentiment.py ./datasets/input-simple.txt ./output/output-simple.txt
```

### Analyse sentiment over time

To run the sentiment analysis over time, run the following command:

```bash
poetry run python ./ng_nltk_playground/sentiment_trends.py ./datasets/input-transcript.txt 
```

### Summarisation

First download the model:

```bash
poetry run python -m spacy download en_core_web_sm
```

Then run it:

```bash
poetry run python ./ng_nltk_playground/summarise.py ./datasets/input-article.txt
```