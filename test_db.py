from database import save_prediction, get_history

save_prediction("I love Python", "Positive")
save_prediction("Worst movie ever", "Negative")

history = get_history()

for row in history:
    print(row)