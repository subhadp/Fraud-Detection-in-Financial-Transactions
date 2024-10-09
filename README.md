# Fraud Detection in Financial Transactions

## Problem Statement
The objective of this project is to develop a machine learning model capable of detecting fraudulent financial transactions in real-time. This solution will help enhance the security of financial systems by identifying suspicious activity promptly.

## Group Members
1. GAURAV BALYAN
2. TANYA BANSAL
3. KHUSHBOO GUPTA
4. RAKKIAPPAN P
5. SUBHADEEP ROY

## Teachers & TAs
1. SHRISTY KAPOOR
2. DHRUV MOHAN
3. DESHMUKH SUDARSHAN S

## Introduction
Financial fraud is a significant issue that results in substantial financial losses for organizations and individuals. By implementing real-time fraud detection, financial institutions can improve their security protocols and protect against potential fraudulent activities. This project involves building a machine learning model that efficiently identifies fraudulent transactions.

## Relevance
The importance of fraud detection cannot be overstated, as it is a vital part of protecting both customers and financial institutions from fraud. Early detection and prevention are essential to reducing the financial and reputational impact of fraudulent activities.

## Data Source
The data used in this project comes from a Financial Transactions Dataset. This dataset contains detailed transaction records, including labels that indicate whether a transaction is fraudulent or legitimate.

## How to Run the Project
1. Clone the repository using:
   ```bash
   git clone https://github.com/subhadp/Fraud-Detection-in-Financial-Transactions.git
2. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
3. Run FASTAPI:
   ```bash
   uvicorn src.api.main:app --reload

# FAST API Output

## Logistic Regression Model
<img width="640" alt="image" src="https://github.com/user-attachments/assets/ef0989a6-0ff1-4187-89bf-5c6e4f8f0f8a">

## Decision Tree Model

<img width="640" alt="image" src="https://github.com/user-attachments/assets/71dd7c74-94c8-48d2-86df-a5e9972f573c">

## CatBoostClassifier Model

<img width="640" alt="image" src="https://github.com/user-attachments/assets/010c3a4b-0610-4599-b3fa-d537681e2be4">

