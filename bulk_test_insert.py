import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('tweets.db')

# Some sample named entities and sentences
entities = ['Tesla', 'Apple', 'Google', 'Microsoft', 'Amazon', 'OpenAI', 'SpaceX', 'Meta']
templates = [
    "I love using {} products!",
    "{} just announced something amazing.",
    "So impressed by what {} is doing lately!",
    "The new {} launch was incredible!",
    "{} is taking over the tech world.",
    "Big win for {} today!",
    "I'm excited about what {} has planned next."
]

# Generate 50 random tweets
for i in range(100, 150):
    entity = random.choice(entities)
    text = random.choice(templates).format(entity)
    sentiment = "positive"
    conn.execute("INSERT OR IGNORE INTO tweets (id, text, sentiment, named_entities) VALUES (?, ?, ?, ?)",
                 (i, text, sentiment, entity))

conn.commit()
conn.close()

print("✅ 50 test tweets inserted.")
