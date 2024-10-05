import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Path to the saved model
MODEL_PATH = os.path.join("models", "model.pkl")

# Load the model
model = joblib.load(MODEL_PATH)

def make_prediction(data: pd.DataFrame):
    # Preprocessing: Assume data is preprocessed similarly as training data
    predictions = model.predict(data)
    return predictions.tolist()
