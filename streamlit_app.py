import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="LaclauGPT Demo",
    page_icon=":alien:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:tomi.toivio@helsinki.fi',
        'Report a bug': "mailto:tomi.toivio@helsinki.fi",
        'About': "LaclauGPT by Tomi Toivio."
    }
)

st.title("LaclauGPT Dev App")
st.write("This is a simple Streamlit app to demonstrate LaclauGPT's capabilities.")

