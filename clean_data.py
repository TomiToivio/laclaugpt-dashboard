import pandas as pd

df = pd.read_csv("mastodon.csv")

# Drop status_json column if it exists
# Only use columns "status_url", "status_date", "status_text", "status_url", "status_username", "political_themes", "political_analysis", "political_entities", "political_topics", "positive_sentiments", "neutral_sentiments", "negative_sentiments"
# Drop all other columns


# Convert 'created_at' to datetime
df['status_date'] = pd.to_datetime(df['status_date'], errors='coerce')
# Convert all columns to string type
for col in df.columns:
    df[col] = df[col].astype(str)

# Save the cleaned data to a new CSV file
df.to_csv("mastodon.csv", index=False)