from fastapi import APIRouter, File, UploadFile, HTTPException
from src.api.models import PredictionResponse
from src.model.predict_model import make_prediction
import pandas as pd
from io import BytesIO

router = APIRouter()


@router.post("/predict/{model_name}", response_model=PredictionResponse)
async def predict(model_name: str, file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")
    contents = await file.read()
    df = pd.read_csv(BytesIO(contents))
    predictions = make_prediction(model_name, df)
    return PredictionResponse(predictions=predictions)
