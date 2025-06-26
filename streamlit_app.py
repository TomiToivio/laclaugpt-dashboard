import streamlit as st
import pandas as pd


st.set_page_config(page_title="LaclauGPT - Social Media Video Analysis",page_icon=":alien:",layout="wide",initial_sidebar_state="expanded",menu_items={
        'Get Help': 'https://github.com/TomiToivio/laclaugpt-dashboard-development',
        'Report a bug': "https://github.com/TomiToivio/laclaugpt-dashboard-development/issues",
        'About': "Developed by Tomi Toivio, University of Helsinki."
    })
# Load data
@st.cache_data

def load_data():
    return pd.read_csv("mastodon.csv")

df = load_data()

st.title("LaclauGPT - Social Media Video Analysis")
st.subheader("Analyze and visualize social media video data with LaclauGPT")

search_query = st.sidebar.text_input("Search:")

start_date = st.sidebar.date_input("Start date", value=df["status_date"].min())
end_date = st.sidebar.date_input("End date", value=df["status_date"].max())

# COnvert 'status_date' to datetime if not already
if not pd.api.types.is_datetime64_any_dtype(df['status_date']):
    df['status_date'] = pd.to_datetime(df['status_date'], errors='coerce')

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
with tab2:
    st.header("Topic Modeling")
with tab3:
    st.header("Entity Recognition")


st.caption("LaclauGPT - Social Media Video Analysis")