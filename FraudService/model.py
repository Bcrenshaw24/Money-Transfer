import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import joblib


np.random.seed(42) 
fraudData = pd.read_csv("data/fraud_data.csv")
N = 1000 

fraudData = fraudData.sample(N, random_state=42).reset_index(drop=True) 

data = fraudData.drop(columns=["isFraud", "transaction_id"])
target = fraudData["isFraud"] 

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42) 

smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

neg, pos = np.bincount(y_train)
scale_pos_weight = (neg / pos) + 6

model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', scale_pos_weight=scale_pos_weight)
model.fit(X_train, y_train) 

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred)) 

joblib.dump(model, "fraud_xgb_model.joblib")


