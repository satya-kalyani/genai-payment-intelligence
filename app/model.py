def load_model():
    class DummyModel:
        def predict(self, data):
            return [0]  # always not fraud
    return DummyModel()
