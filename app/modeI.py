from sklearn.ensemble import RandomForestClassifier
import numpy as np

def load_model():
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)
    
    model = RandomForestClassifier()
    model.fit(X, y)
    return model
