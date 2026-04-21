@app.post("/predict")
def predict(data: list):
    prediction = model.predict([data])
    return {"fraud": int(prediction[0])}
