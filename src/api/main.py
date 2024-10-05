from fastapi import FastAPI
from src.api.routes import router as api_router

app = FastAPI(title="Machine Learning Fraud Detection in Financial Transactions API")

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the ML Fraud Detection in Financial Transactions API"}
