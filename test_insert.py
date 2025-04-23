import sqlite3

conn = sqlite3.connect('tweets.db')

sample_tweets = [
    (1, "I love my new Tesla car!", "positive", "Tesla"),
    (2, "Google just released something amazing.", "positive", "Google"),
    (3, "Microsoft is doing great lately!", "positive", "Microsoft")
]

for tweet_id, text, sentiment, entities in sample_tweets:
    conn.execute("INSERT OR IGNORE INTO tweets (id, text, sentiment, named_entities) VALUES (?, ?, ?, ?)",
                 (tweet_id, text, sentiment, entities))

conn.commit()
conn.close()

print("Test tweets inserted.")
