import pandas as pd
import re
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def clean_text(text):
    text = text.lower()              # sab kuch lowercase me
    text = re.sub(r'\W', ' ', text)  # special characters hata do
    text = re.sub(r'\s+', ' ', text) # extra spaces hata do
    return text

def train_model():
    # CSV file padho
    data = pd.read_csv("spam.csv", encoding='latin-1')[['v1', 'v2']]
    data.columns = ['label', 'message']  # column names rename karo

    # Labels ko 0 (ham) aur 1 (spam) me convert karo
    data['label'] = data['label'].map({'ham': 0, 'spam': 1})

    # Messages ko clean karo
    data['cleaned_message'] = data['message'].apply(clean_text)

    # Text ko numbers me convert karo
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data['cleaned_message'])
    y = data['label']

    # Train/test data split karo
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Naive Bayes model train karo
    model = MultinomialNB()
    model.fit(x_train, y_train)

    # Trained model aur vectorizer return karo
    return model, vectorizer

#flask

def save_model(model, vectorizer):
    joblib.dump(model, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

# ✅ Make sure this is at the bottom:
if __name__ == "__main__":
    model, vectorizer = train_model()
    save_model(model, vectorizer)
    print("Model and vectorizer saved successfully!")