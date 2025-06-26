import pandas as pd
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')

mongo_client = pymongo.MongoClient(MONGO_URL)
mongo_database = mongo_client["spectacleScraper"]
mongo_collection = mongo_database["noosphere_mastodon"]

df = pd.DataFrame(columns=["status_url", "status_date", "status_text", "status_url", "status_username", "political_themes", "political_analysis", "political_entities", "political_topics", "positive_sentiments", "neutral_sentiments", "negative_sentiments"])

documents = mongo_collection.find()
for document in documents:
    status_url = document.get("status_url", "")
    status_date = document.get("status_date", "")
    status_text = document.get("status_text", "")
    status_username = document.get("status_username", "")
    political_themes = document.get("political_themes", "")
    political_analysis = document.get("political_analysis", "")
    political_entities = document.get("political_entities", "")
    political_topics = document.get("political_topics", "")
    positive_sentiments = document.get("positive_sentiments", "")
    neutral_sentiments = document.get("neutral_sentiments", "")
    negative_sentiments = document.get("negative_sentiments", "")
    # Append the data to the DataFrame
    df.loc[len(df)] = [status_url, status_date, status_text, status_url, status_username, political_themes, political_analysis, political_entities, political_topics, positive_sentiments, neutral_sentiments, negative_sentiments]

# Drop ones where status_text is empty
df = df[df['status_text'].str.strip() != ""]
# Convert all columns to string type
for col in df.columns:
    df[col] = df[col].astype(str)

# Save the DataFrame to a CSV file
df.to_csv("mastodon.csv", index=False)