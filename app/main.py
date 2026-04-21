from fastapi import FastAPI
from model import load_model
from rag import query_rag

app = FastAPI()

# Load model once
model = load_model()

@app.get("/")
def home():
    return {"message": "GenAI Payment Intelligence API is running"}

@app.post("/predict")
def predict(data: list):
    prediction = model.predict([data])
    return {"fraud": int(prediction[0])}

@app.get("/ask")
def ask(query: str):
    response = query_rag(query)
    return {"response": response}
