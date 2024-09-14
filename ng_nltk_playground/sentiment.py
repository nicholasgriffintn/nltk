import nltk
import argparse
import logging
from nltk.sentiment import SentimentIntensityAnalyzer
from concurrent.futures import ThreadPoolExecutor

nltk.download('punkt')
nltk.download('vader_lexicon')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def tokenize_text(text):
    return nltk.word_tokenize(text)

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

def process_sentence(sentence):
    tokens = tokenize_text(sentence)
    sentiment = analyze_sentiment(sentence)
    return {
        'sentence': sentence,
        'tokens': tokens,
        'sentiment': sentiment
    }

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"Error: The file at {file_path} could not be found.")
    except IOError as e:
        logging.error(f"Error reading the file at {file_path}: {e}")
    return None

def write_results(output_file, results):
    try:
        with open(output_file, 'w') as file:
            for result in results:
                file.write(f"Sentence: {result['sentence']}\n")
                file.write(f"Tokens: {result['tokens']}\n")
                file.write(f"Sentiment: {result['sentiment']}\n\n")
    except IOError as e:
        logging.error(f"Error writing to the file at {output_file}: {e}")

def process_file(input_file, output_file):
    text = read_file(input_file)
    if text is None:
        return

    sentences = nltk.sent_tokenize(text)
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_sentence, sentences))

    write_results(output_file, results)
    logging.info("Processing complete.")

def interactive_mode():
    print("Enter text (type 'exit' to quit):")
    while True:
        text = input("> ")
        if text.lower() == 'exit':
            break
        result = process_sentence(text)
        print(f"Tokens: {result['tokens']}")
        print(f"Sentiment: {result['sentiment']}")

def main():
    parser = argparse.ArgumentParser(description="Tokenize text and perform sentiment analysis.")
    parser.add_argument('--input_file', type=str, help="Path to the input text file.")
    parser.add_argument('--output_file', type=str, help="Path to the output file to save results.")
    parser.add_argument('--interactive', action='store_true', help="Run in interactive mode.")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.input_file and args.output_file:
        process_file(args.input_file, args.output_file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()