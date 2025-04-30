import streamlit as st
import pandas as pd
from models import train_random_forest, train_gb_regressor

def app():
    st.title("\U0001F52C Model Training")
    st.markdown("Upload a dataset and train machine learning models.")

    uploaded = st.file_uploader("Upload CSV for Training", type="csv")
    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df.head())

        features = st.multiselect("Select Features", df.columns)
        target = st.selectbox("Select Target Variable", df.columns)

        if st.button("Train Classification Model"):
            model, report = train_random_forest(df[features], df[target])
            st.text("Classification Report:")
            st.text(report)

        if st.button("Train Regression Model"):
            model, mse = train_gb_regressor(df[features], df[target])
            st.text(f"Mean Squared Error: {mse}")
