import streamlit as st
import pandas as pd

def laclaugpt_dashboard():
    st.dataframe(df)
    tab1, tab2, tab3 = st.tabs(["Sentiments", "Topics", "Entities"])
    with tab1:
        st.header("Sentiment Analysis")
    with tab2:
        st.header("Topic Modeling")
    with tab3:
        st.header("Entity Recognition")

def laclaugpt_sidebar():


st.set_page_config(
    page_title="LaclauGPT - Social Media Video Analysis",
    page_icon=":alien:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/TomiToivio/laclaugpt-dashboard-development',
        'Report a bug': "https://github.com/TomiToivio/laclaugpt-dashboard-development/issues",
        'About': "Developed by Tomi Toivio, University of Helsinki."
    }
)
# Load data
@st.cache_data

def load_data():
    return pd.read_csv("mastodon.csv")

df = load_data()

st.title("LaclauGPT - Social Media Video Analysis")
st.subheader("Analyze and visualize social media video data with LaclauGPT")

st.dataframe(df)

tab1, tab2, tab3 = st.tabs(["Sentiments", "Topics", "Entities"])
with tab1:
    st.header("Sentiment Analysis")
with tab2:
    st.header("Topic Modeling")
with tab3:
    st.header("Entity Recognition")


st.caption("LaclauGPT - Social Media Video Analysis")