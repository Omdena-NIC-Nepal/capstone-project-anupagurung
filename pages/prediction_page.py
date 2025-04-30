import streamlit as st
from prediction import load_model, predict

def app():
    st.title("\U0001F52E Prediction")
    model_path = st.text_input("Enter full path to .joblib model file")
    
    if model_path:
        try:
            model = load_model(model_path)
            inputs = st.text_input("Enter comma-separated input values")
            if st.button("Predict"):
                input_data = list(map(float, inputs.split(",")))
                result = predict(model, input_data)
                st.success(f"Prediction Result: {result[0]}")
        except Exception as e:
            st.error(f"Failed to load model or make prediction: {e}")