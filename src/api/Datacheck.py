import sklearn
import joblib
print(sklearn.__version__)
print(joblib.__version__)


import joblib
model = joblib.load(r'D:\fraud_detection_dataset\Fraud-Detection-in-Financial-Transactions\models\logistic_regression_model.pkl')
