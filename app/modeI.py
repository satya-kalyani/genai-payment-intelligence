import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

MODEL_PATH = "model.pkl"

def train_model():
    df = pd.read_csv("data/sample_transactions.csv")
    X = df.drop("fraud", axis=1)
    y = df["fraud"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    return model

def load_model():
    if not os.path.exists(MODEL_PATH):
        return train_model()
    return joblib.load(MODEL_PATH)
