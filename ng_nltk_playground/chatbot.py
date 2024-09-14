import nltk
import random
import spacy

nltk.download('punkt')
nltk.download('stopwords')

nlp = spacy.load('en_core_web_sm')

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return tokens

def generate_response(user_input):
    responses = {
        'hello': [
            "Hi there! How can I help you today?",
            "Hello! What can I do for you?",
            "Hey! How's it going?"
        ],
        'bye': [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! Hope to chat with you soon!"
        ],
        'name': [
            "I'm a chatbot created to assist you.",
            "You can call me Chatbot.",
            "I'm your friendly assistant chatbot."
        ],
        'help': [
            "Sure, I'm here to help. What do you need assistance with?",
            "How can I assist you today?",
            "What do you need help with?"
        ],
        'feel': [
            "I'm just a bunch of code, but I'm here to help you!",
            "I don't have feelings, but I'm here to assist you!",
            "I'm here to help you with whatever you need!"
        ]
    }
    
    for word in user_input:
        if word in responses:
            return random.choice(responses[word])
    
    return "I'm not sure I understand. Can you tell me more?"

def chatbot():
    print("Hello! I'm a chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        tokens = preprocess(user_input)
        response = generate_response(tokens)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()