import streamlit as st
import pandas as pd


st.set_page_config(page_title="LaclauGPT - Social Media Video Analysis",page_icon=":alien:",layout="wide",initial_sidebar_state="expanded",menu_items={
        'Get Help': 'https://github.com/TomiToivio/laclaugpt-dashboard',
        'Report a bug': "https://github.com/TomiToivio/laclaugpt-dashboard/issues",
        'About': "Developed by Tomi Toivio, University of Helsinki."
    })
# Load data
@st.cache_data

def load_data():
    return pd.read_csv("mastodon.csv")

df = load_data()

st.title("LaclauGPT - Social Media Video Analysis")
st.subheader("Analyze and visualize social media video data with LaclauGPT")

# Force status_date to datetime
if not pd.api.types.is_datetime64_any_dtype(df['status_date']):
    df['status_date'] = pd.to_datetime(df['status_date'], errors='coerce')

search_query = st.sidebar.text_input("Search:")

start_date = st.sidebar.date_input("Start date", value=df["status_date"].min())
end_date = st.sidebar.date_input("End date", value=df["status_date"].max())

filtered_df = df.copy()

filtered_df = filtered_df[(filtered_df["status_date"] >= pd.to_datetime(start_date)) & (filtered_df["status_date"] <= pd.to_datetime(end_date))]

if search_query:
    filtered_df = filtered_df[filtered_df.apply(lambda row: row.astype(str).str.contains(search_query, case=False, na=False).any(), axis=1)]

st.dataframe(filtered_df)

total_count = len(df)
filtered_count = len(filtered_df)
st.write(f"Viewing {filtered_count} out of {total_count} statuses.")

tab1, tab2, tab3 = st.tabs(["Sentiments", "Topics", "Entities"])
with tab1:
    st.header("Sentiment Analysis")
    positive_series = filtered_df["positive_sentiments"].dropna().str.split(", ").explode()
    negative_series = filtered_df["negative_sentiments"].dropna().str.split(", ").explode()
    neutral_series = filtered_df["neutral_sentiments"].dropna().str.split(", ").explode()
    #positive_daily_counts = filtered_df.groupby(["status_date", "positive_sentiments"]).size().unstack(fill_value=0)
    #negative_daily_counts = filtered_df.groupby(["status_date", "negative_sentiments"]).size().unstack(fill_value=0)
    #neutral_daily_counts = filtered_df.groupby(["status_date", "neutral_sentiments"]).size().unstack(fill_value=0)
    #chart_data = pd.DataFrame({
    #    "Positive": positive_daily_counts.sum(axis=1),
    #    "Negative": negative_daily_counts.sum(axis=1),
    #    "Neutral": neutral_daily_counts.sum(axis=1)
    #})
    # Plot daily positive, negative, and neutral sentiment counts
    #st.line_chart(chart_data)
    top_positive = positive_series.value_counts().head(20)
    top_negative = negative_series.value_counts().head(20)
    top_neutral = neutral_series.value_counts().head(20)
    # Positive chart
    st.subheader("Top Positive Sentiments")
    st.bar_chart(top_positive)
    # Negative chart
    st.subheader("Top Negative Sentiments")
    st.bar_chart(top_negative)
    #sentiment_df = pd.DataFrame({
    #    "Positive": top_positive,
    #    "Negative": top_negative,
    #    "Neutral": top_neutral
    #}).fillna(0).astype(int)
    #sentiment_df = sentiment_df.sort_values(by=["Positive", "Negative", "Neutral"], ascending=False)
    #st.dataframe(sentiment_df)
    # Get a count of each unique sentiment and combine them into a single DataFrame
    sentiment_counts = pd.concat([positive_series, negative_series, neutral_series]).value_counts()
    # Also count negative, positive, and neutral sentiment for each sentiment    
    # Show all sentiments with their counts
    sentiment_counts_df = pd.DataFrame(sentiment_counts).reset_index()
    sentiment_counts_df.columns = ["Sentiment", "Count"]
    sentiment_counts_df = sentiment_counts_df.sort_values(by="Count", ascending=False)
    st.dataframe(sentiment_counts_df)


with tab2:
    st.header("Topic Modeling")
    topics_series = filtered_df["political_topics"].dropna().str.split(", ").explode()
    top_topics = topics_series.value_counts().head(20)
    st.subheader("Top Political Topics")
    st.bar_chart(top_topics)
    #topic_df = pd.DataFrame([{"topic": topic, "count": count} for topic, count in top_topics.items()])
    #topic_df = topic_df.sort_values(by="count", ascending=False)
    # Get a count of each unique topic
    topic_counts = topics_series.value_counts()
    # Show all topics with their counts
    topic_counts_df = pd.DataFrame(topic_counts).reset_index()
    topic_counts_df.columns = ["Topic", "Count"]
    st.dataframe(topic_counts_df)

with tab3:
    st.header("Entity Recognition")
    entities_series = filtered_df["political_entities"].dropna().str.split(", ").explode()
    top_entities = entities_series.value_counts().head(20)
    #entity_df = pd.DataFrame([{"entity": entity, "count": count} for entity, count in top_entities.items()])
    #entity_df = entity_df.sort_values(by="count", ascending=False)
    st.subheader("Top Political Entities")
    st.bar_chart(top_entities)
    # Get a count of each unique entity
    entity_counts = entities_series.value_counts()
    # Show all entities with their counts
    entity_counts_df = pd.DataFrame(entity_counts).reset_index()
    entity_counts_df.columns = ["Entity", "Count"]
    st.dataframe(entity_counts_df)


st.caption("LaclauGPT - Social Media Video Analysis")