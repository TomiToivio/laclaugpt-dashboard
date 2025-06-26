import streamlit as st
import pandas as pd

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

st.title("LaclauGPT - Social Media Video Analysis")
st.subheader("Analyze and visualize social media video data with LaclauGPT")

st.caption("LaclauGPT - Social Media Video Analysis")