import joblib 
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import sys
import os


class predict_pip:
    def predict1(self,features):
        # model = joblib.load(r".\artifacts\best_model.pkl")
        model = joblib.load('/app/artifacts/best_model.pkl')
        y = model.predict(features)
        return y 