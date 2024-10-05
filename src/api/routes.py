from fastapi import APIRouter, File, UploadFile, HTTPException
from src.api.models import PredictionResponse
from src.model.predict_model import make_prediction
import pandas as pd
from io import BytesIO

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    # Ensure the uploaded file is a CSV
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")

    # Read the uploaded CSV file into a pandas DataFrame
    contents = await file.read()
    df = pd.read_csv(BytesIO(contents))

    # Call the prediction function from the predict_model.py
    predictions = make_prediction(df)

    return {"predictions": predictions}
