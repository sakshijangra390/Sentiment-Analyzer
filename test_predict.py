from predict import predict_sentiment

while True:
    text = input("Enter text: ")

    if text.lower() == "quit":
        break

    result = predict_sentiment(text)

    print("Prediction:", result)