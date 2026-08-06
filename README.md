# Sentiment-Analyzer

# 😊 AI Sentiment Analyzer using Python, Flask & Machine Learning

An AI-powered Sentiment Analysis web application developed using **Python**, **Flask**, **Machine Learning**, and **Natural Language Processing (NLP)**. The application analyzes user text and predicts whether the sentiment is **Positive**, **Negative**, or **Neutral**.

---

## 📌 Features

- 😊 Predicts Positive, Negative, and Neutral sentiments
- 🤖 Machine Learning model using Logistic Regression
- 🧠 Natural Language Processing (NLP)
- 📊 TF-IDF Vectorization
- 💾 Stores prediction history using SQLite
- 🌐 Flask-based web application
- 📱 Responsive and user-friendly interface
- 📜 View previous prediction history

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- SQLite
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Joblib

---

## 🤖 Machine Learning Workflow

```
User Input
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Logistic Regression Model
      │
      ▼
Sentiment Prediction
      │
      ▼
Save Result to SQLite Database
```

---

## 📂 Project Structure

```
Sentiment-Analyzer/
│
├── app.py
├── train_model.py
├── predict.py
├── database.py
├── requirements.txt
├── model.pkl
├── vectorizer.pkl
├── sentiment.db
│
├── dataset/
│   └── sentiment.csv
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── result.html
│   └── history.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Sentiment-Analyzer.git
```

### 2️⃣ Go to the project folder

```bash
cd Sentiment-Analyzer
```

### 3️⃣ Create a virtual environment

```bash
python -m venv myenv
```

### 4️⃣ Activate the virtual environment

**Windows**

```bash
myenv\Scripts\activate
```

### 5️⃣ Install the required packages

```bash
pip install -r requirements.txt
```

### 6️⃣ Train the model (if model files are not included)

```bash
python train_model.py
```

### 7️⃣ Run the Flask application

```bash
python app.py
```

### 8️⃣ Open your browser

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

You can add screenshots of:

- 🏠 Home Page
- 😊 Prediction Result
- 📜 Prediction History

---

## 📖 Future Enhancements

- 📊 Confidence Score
- 📈 Sentiment Charts
- 🌙 Dark Mode
- 🔐 User Authentication
- 📄 Export History to CSV/PDF
- 🎤 Voice Input
- 🌍 Multi-language Support
- ☁️ Deploy on Render or Railway

---

## 🎯 Learning Outcomes

This project demonstrates:

- Natural Language Processing (NLP)
- Text Preprocessing
- Machine Learning Classification
- TF-IDF Vectorization
- Logistic Regression
- Flask Web Development
- SQLite Database Integration
- Model Deployment

---


## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is created for educational and learning purposes.
