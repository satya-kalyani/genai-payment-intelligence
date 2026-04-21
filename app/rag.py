def query_rag(query: str):
    docs = [
        "Fraud detection uses transaction patterns",
        "High-value transactions are riskier",
        "Frequent location changes may indicate fraud"
    ]
    
    for doc in docs:
        if any(word in doc.lower() for word in query.lower().split()):
            return doc
    
    return "No relevant info found"
