import joblib
import numpy as np

def load_model(path):
    return joblib.load(path)

def predict(model, input_data):
    return model.predict(np.array(input_data).reshape(1, -1))

