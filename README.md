# GenAI Payment Intelligence System

AI-powered system for fraud detection and intelligent querying of financial transactions using machine learning and generative AI.

---

## Overview

This project simulates a production-style fintech system combining fraud detection models with retrieval-augmented generation (RAG) for intelligent querying.

---

## Features

* Fraud detection using machine learning models
* RAG-based chatbot for transaction insights
* FastAPI-based REST APIs
* Dockerized deployment
* Scalable architecture design

---

## Architecture

User → FastAPI → ML Model + RAG → Response

---

## Tech Stack

* Python
* Scikit-learn / PyTorch
* LangChain + FAISS
* FastAPI
* Docker

---

## How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## API Endpoints

Fraud Prediction
POST /predict

Query System
GET /ask?query=your_question

---

## Example

Request:

```json
{
  "amount": 250,
  "location": "NY"
}
```

Response:

```json
{
  "fraud": 0
}
```

---

## Screenshots

Add screenshots here

---

## Status

In progress

---

## Future Improvements

* Real-time streaming with Kafka
* AWS deployment (SageMaker / ECS)
* Advanced LLM fine-tuning
* Monitoring with Prometheus and Grafana
