import joblib
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Initialize NLP tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


def preprocess(text):
    """
    Clean and preprocess user input.
    """
    words = nltk.word_tokenize(text.lower())

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word.isalnum() and word not in stop_words
    ]

    return " ".join(words)


def predict_sentiment(text):
    """
    Predict sentiment of input text.
    Returns:
        sentiment (Positive/Negative/Neutral)
    """

    clean_text = preprocess(text)

    vector = vectorizer.transform([clean_text])

    prediction = model.predict(vector)[0]

    return prediction