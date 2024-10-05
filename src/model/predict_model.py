import pandas as pd
import joblib
import os

MODELS_DIR = r"D:\fraud_detection_dataset\Fraud-Detection-in-Financial-Transactions\models"
MODEL_FILENAMES = {
    "logistic_regression": os.path.join(MODELS_DIR, "logistic_regression_model.pkl"),
    "decision_tree": os.path.join(MODELS_DIR, "decision_tree_model.pkl"),
    "dnn": os.path.join(MODELS_DIR, "DNN_model.pkl"),
}

models = {name: joblib.load(path) for name, path in MODEL_FILENAMES.items()}


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    # Implement preprocessing steps here
    data = pd.get_dummies(data, columns=['type', 'nameOrig', 'nameDest'], drop_first=True)

    # Ensure all required numeric columns are present
    required_columns = ['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']

    for column in required_columns:
        if column not in data.columns:
            data[column] = 0  # Add missing columns with default value 0

    # Reorder columns to match model expectations
    data = data[required_columns + [col for col in data.columns if col not in required_columns]]

    return data


def make_prediction(model_name: str, data: pd.DataFrame):
    if model_name not in models:
        raise ValueError("Model not found. Available models: " + ", ".join(models.keys()))

    processed_data = preprocess_data(data)
    predictions = models[model_name].predict(processed_data)
    return predictions.tolist()
