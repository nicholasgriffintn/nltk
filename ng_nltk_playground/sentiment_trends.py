import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt
import argparse

def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {file_path} could not be found.")
        return None

def split_into_sentences(transcript):
    return nltk.sent_tokenize(transcript)

def evaluate_sentiment(sentences):
    return [TextBlob(sentence).sentiment.polarity for sentence in sentences]

def display_sentiment_trends(sentiments, output_path=None):
    plt.plot(sentiments)
    plt.xlabel('Sentence Index')
    plt.ylabel('Sentiment Polarity')
    plt.title('Sentiment Trends Throughout the Transcript')
    if output_path:
        plt.savefig(output_path)
        print(f"Sentiment trend plot has been saved to {output_path}")
    else:
        plt.show()

def analyze_transcript(file_path, output_path=None):
    transcript = read_file_content(file_path)
    if transcript is None:
        return
    
    sentences = split_into_sentences(transcript)
    sentiments = evaluate_sentiment(sentences)
    display_sentiment_trends(sentiments, output_path)

def main():
    parser = argparse.ArgumentParser(description="Analyze sentiment trends over a transcript.")
    parser.add_argument('file_path', type=str, help="Path to the transcript file.")
    parser.add_argument('--output_file', type=str, help="Path to save the sentiment trend plot image.")
    args = parser.parse_args()
    
    analyze_transcript(args.file_path, args.output_file)

if __name__ == "__main__":
    main()