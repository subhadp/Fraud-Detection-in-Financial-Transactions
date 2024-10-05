import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML Fraud Detection in Financial Transactions API"}


def test_predict_valid_csv():
    # Create a mock CSV file as a string
    data = """step,type,amount,nameOrig,oldbalanceOrg,newbalanceOrig,nameDest,oldbalanceDest,newbalanceDest,isFraud,isFlaggedFraud
    1,TRANSFER,1000.0,A,B,C,D,E,F,G,H
    """

    response = client.post("/predict", files={"file": ("test.csv", data)})
    assert response.status_code == 200
    assert "predictions" in response.json()


def test_predict_invalid_file_type():
    # Create a mock non-CSV file
    data = "This is not a CSV file."

    response = client.post("/predict", files={"file": ("test.txt", data)})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid file type. Please upload a CSV file."}


def test_predict_missing_columns():
    # Create a mock CSV file missing required columns
    data = """step,type,amount,nameOrig
    1,TRANSFER,1000.0,A
    """
    response = client.post("/predict", files={"file": ("test.csv", data)})
    assert response.status_code == 400
    assert response.json() == {"detail": "CSV missing required columns."}
