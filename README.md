# GenAI Payment Intelligence System

Designed as a scalable backend system demonstrating real-world ML and GenAI integration.

---

## Overview

This project implements a fintech intelligence system that combines machine learning–based fraud detection with a retrieval-augmented generation (RAG) pipeline to enable intelligent querying of financial transaction data.

---

## Features

* Fraud detection using supervised ML models trained on transaction features
* Retrieval-Augmented Generation (RAG) for contextual query responses
* FastAPI-based REST APIs
* Dockerized deployment
* Scalable and modular architecture

---

## Architecture

User → FastAPI API Layer → ML Model + RAG Engine → Response

Lightweight backend architecture designed for scalability and modular ML/LLM integration.

---

## Tech Stack

* Python
* Scikit-learn
* FastAPI
* Docker

---

## How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open in browser:
http://127.0.0.1:8000/docs

---

## API Endpoints

### Fraud Prediction

POST /predict

### Query System

GET /ask?query=your_question

---

## Example

### Request

```json
[0.2, 0.5, 0.1, 0.9, 0.3]
```

### Response

```json
{
  "fraud": 0
}
```

---

## Screenshots

API Documentation (FastAPI Swagger UI)

![API](assets/api.png)
---

## Status

In progress

---

## Future Improvements

* Real-time streaming with Kafka
* AWS deployment (SageMaker / ECS)
* Advanced LLM fine-tuning
* Monitoring with Prometheus and Grafana

