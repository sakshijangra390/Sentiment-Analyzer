import sqlite3


def create_database():
    conn = sqlite3.connect("sentiment.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_prediction(text, sentiment):
    conn = sqlite3.connect("sentiment.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history(text, sentiment) VALUES (?, ?)",
        (text, sentiment)
    )

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect("sentiment.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM history ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_history():
    conn = sqlite3.connect("sentiment.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM history")

    conn.commit()
    conn.close()


create_database()