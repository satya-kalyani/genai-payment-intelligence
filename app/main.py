from fastapi import FastAPI
from pydantic import BaseModel
from app.model import load_model
from app.rag import query_rag

app = FastAPI()

model = load_model()

class InputData(BaseModel):
    data: list

@app.get("/")
def home():
    return {"message": "GenAI Payment Intelligence API is running"}

@app.post("/predict")
def predict(input: InputData):
    prediction = model.predict([input.data])
    return {"fraud": int(prediction[0])}

@app.get("/ask")
def ask(query: str):
    response = query_rag(query)
    return {"response": response}
