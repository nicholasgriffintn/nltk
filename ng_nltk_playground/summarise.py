import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import spacy
import argparse
import os

nltk.download('punkt')
nltk.download('stopwords')

nlp = spacy.load("en_core_web_sm")

def generate_summary(text, num_sentences=5):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    word_freq = nltk.FreqDist(filtered_words)
    
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]
    
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(top_sentences)

def identify_entities(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        entities.setdefault(ent.label_, []).append(ent.text)
    return entities

def get_pos_tags(text):
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

def handle_article(file_path, output_path=None, num_sentences=5):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return
    
    summary = generate_summary(text, num_sentences)
    entities = identify_entities(text)
    pos_tags = get_pos_tags(text)
    
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as file:
            file.write("Summary:\n")
            file.write(summary + "\n\n")
            file.write("Named Entities:\n")
            for label, ents in entities.items():
                file.write(f"{label}: {', '.join(ents)}\n")
            file.write("\nPOS Tags:\n")
            for word, pos in pos_tags:
                file.write(f"{word}: {pos}\n")
        print(f"Summary, entities, and POS tags saved to {output_path}")
    else:
        print("Summary:")
        print(summary)
        print("\nNamed Entities:")
        for label, ents in entities.items():
            print(f"{label}: {', '.join(ents)}")
        print("\nPOS Tags:")
        for word, pos in pos_tags:
            print(f"{word}: {pos}")

def main():
    parser = argparse.ArgumentParser(description="Summarize an article, extract named entities, and POS tags.")
    parser.add_argument('file_path', type=str, help="Path to the article file.")
    parser.add_argument('--output_path', type=str, help="Path to save the summary, entities, and POS tags.")
    parser.add_argument('--num_sentences', type=int, default=5, help="Number of sentences in the summary.")
    args = parser.parse_args()
    
    handle_article(args.file_path, args.output_path, args.num_sentences)

if __name__ == "__main__":
    main()