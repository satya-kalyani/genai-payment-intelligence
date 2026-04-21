from fastapi import FastAPI
from app.model import load_model
from app.rag import query_rag

app = FastAPI()

model = load_model()

@app.get("/")
def home():
    return {"message": "GenAI Payment Intelligence API"}

@app.post("/predict")
def predict(data: dict):
    prediction = model.predict([list(data.values())])
    return {"fraud": int(prediction[0])}

@app.get("/ask")
def ask(query: str):
    response = query_rag(query)
    return {"response": response}
