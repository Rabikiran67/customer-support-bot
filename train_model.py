import json
import random
import pickle
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')
with open('intents.json') as f:
    data = json.load(f)

texts, labels = [], []
for intent in data['intents']:
    for pattern in intent['patterns']:
        texts.append(pattern)
        labels.append(intent['tag'])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
clf = LogisticRegression()
clf.fit(X, labels)

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model trained and saved.")
