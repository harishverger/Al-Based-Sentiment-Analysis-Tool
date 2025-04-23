import matplotlib.pyplot as plt
from Analizer2_with_DBconnection import TweetAnalyzer

# Choose the sentiment: 'positive', 'negative', or 'neutral'
sentiment = 'negative'

# Create analyzer and fetch top named entities
analyzer = TweetAnalyzer('tweets.db')
top_named_entities = analyzer.get_top_named_entities(sentiment=sentiment, num_entities=10)

if not top_named_entities:
    print(f"No named entities found for sentiment: {sentiment}")
    exit()

# Separate data for plotting
named_entities = [ne[0] for ne in top_named_entities]
frequencies = [ne[1] for ne in top_named_entities]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(named_entities, frequencies, color='skyblue')
ax.set_xlabel('Frequency')
ax.set_ylabel('Named Entity')
ax.set_title(f'Top Named Entities in {sentiment.capitalize()} Tweets')
ax.invert_yaxis()  # Highest at top

# Save the chart as PNG
plt.tight_layout()
plt.savefig(f'top_named_entities_{sentiment}.png')
print(f"✅ Chart saved as top_named_entities_{sentiment}.png")

# Show the plot
plt.show()
