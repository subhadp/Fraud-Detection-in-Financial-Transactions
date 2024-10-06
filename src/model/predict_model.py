import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

MODEL_FILENAMES = {
    "LOG": r".\.\models\logistic_regression_model.pkl",
    "DS": r".\.\models\decision_tree_model.pkl",
    "CB": r".\.\models\CatBoost_Model.pkl"
}

models = {name: joblib.load(path) for name, path in MODEL_FILENAMES.items()}


def make_prediction(model_name: str, data: pd.DataFrame):
    if model_name not in models:
        raise ValueError("Model not found. Available models: " + ", ".join(models.keys()))
    print(f"Shape of data before prediction: {data.shape}")
    predictions = models[model_name].predict(data)
    print(predictions)
    return predictions.tolist()