import pandas as pd
import nltk
import joblib

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

# Load dataset
data = pd.read_csv("dataset/sentiment.csv")

# Initialize
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Text preprocessing function
def preprocess(text):
    words = nltk.word_tokenize(str(text).lower())
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word.isalnum() and word not in stop_words
    ]
    return " ".join(words)

# Clean text
data["clean_text"] = data["text"].apply(preprocess)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(data["clean_text"])
y = data["sentiment"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("=" * 50)
print("✅ Model trained successfully!")
print("✅ model.pkl saved")
print("✅ vectorizer.pkl saved")
print("=" * 50)