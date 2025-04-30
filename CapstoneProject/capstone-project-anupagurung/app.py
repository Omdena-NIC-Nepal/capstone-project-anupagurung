import streamlit as st
from pages import data_exploration, model_training, prediction_page

st.set_page_config(page_title="Nepal Climate Change Analysis", layout="wide")

PAGES = {
    "Data Exploration": data_exploration,
    "Model Training": model_training,
    "Prediction": prediction_page
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()