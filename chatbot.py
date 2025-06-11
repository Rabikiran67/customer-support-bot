import random
import json
import pickle
import nltk
from nltk.tokenize import word_tokenize

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("intents.json") as f:
    intents = json.load(f)

def get_intent(text):
    X = vectorizer.transform([text])
    return model.predict(X)[0]

def get_response(intent_tag):
    for intent in intents["intents"]:
        if intent["tag"] == intent_tag:
            return random.choice(intent["responses"])
    return "Sorry, I didn't understand that."

def chatbot_response(text):
    intent = get_intent(text)
    return get_response(intent)
