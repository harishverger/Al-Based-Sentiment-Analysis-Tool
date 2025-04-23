import sqlite3
import random
from Analizer2_with_DBconnection import TweetAnalyzer
import matplotlib.pyplot as plt
import os

def insert_sample_tweets():
    conn = sqlite3.connect('tweets.db')
    sample_entities = ['Tesla', 'Apple', 'Google', 'Microsoft', 'Amazon', 'OpenAI', 'SpaceX', 'Meta']
    positive_templates = [
        "I love using {} products!",
        "{} just announced something amazing.",
        "So impressed by what {} is doing lately!",
        "The new {} launch was incredible!"
    ]
    negative_templates = [
        "{} is getting worse each year.",
        "I’m disappointed with {}’s new update.",
        "Why is {} always messing things up?",
        "Bad experience with {} today."
    ]

    print("📝 Inserting sample tweets into database...")
    for i in range(300, 325):
        entity = random.choice(sample_entities)
        text = random.choice(positive_templates).format(entity)
        sentiment = "positive"
        conn.execute("INSERT OR IGNORE INTO tweets (id, text, sentiment, named_entities) VALUES (?, ?, ?, ?)",
                     (i, text, sentiment, entity))

    for i in range(325, 350):
        entity = random.choice(sample_entities)
        text = random.choice(negative_templates).format(entity)
        sentiment = "negative"
        conn.execute("INSERT OR IGNORE INTO tweets (id, text, sentiment, named_entities) VALUES (?, ?, ?, ?)",
                     (i, text, sentiment, entity))

    conn.commit()
    conn.close()
    print("✅ Sample tweets inserted.\n")

def print_named_entities(sentiment='positive'):
    analyzer = TweetAnalyzer('tweets.db')
    top_entities = analyzer.get_top_named_entities(sentiment=sentiment, num_entities=10)

    print(f"📊 Top Named Entities in {sentiment.capitalize()} Tweets:\n")
    for i, (name, count) in enumerate(top_entities, 1):
        print(f"{i:>2}. {name:<15} ➜ {count} mentions")
    print()
    return top_entities

def plot_named_entities(top_entities, sentiment='positive'):
    entities = [ne[0] for ne in top_entities]
    counts = [ne[1] for ne in top_entities]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(entities, counts, color='lightcoral' if sentiment == 'negative' else 'skyblue')
    ax.set_xlabel('Mentions')
    ax.set_ylabel('Entity')
    ax.set_title(f'Top Named Entities in {sentiment.capitalize()} Tweets')
    ax.invert_yaxis()

    filename = f'top_named_entities_{sentiment}.png'
    plt.tight_layout()
    plt.savefig(filename)
    print(f"📁 Chart saved as: {filename}")
    plt.show()

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    insert_sample_tweets()

    for sentiment in ['positive', 'negative']:
        entities = print_named_entities(sentiment=sentiment)
        plot_named_entities(entities, sentiment=sentiment)
