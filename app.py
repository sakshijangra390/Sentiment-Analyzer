from flask import Flask, render_template, request
from predict import predict_sentiment
from database import save_prediction, get_history

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    text = request.form["text"]

    sentiment = predict_sentiment(text)

    save_prediction(text, sentiment)

    return render_template(
        "result.html",
        text=text,
        sentiment=sentiment
    )


@app.route("/history")
def history():

    data = get_history()

    return render_template(
        "history.html",
        history=data
    )


if __name__ == "__main__":
    app.run(debug=True)