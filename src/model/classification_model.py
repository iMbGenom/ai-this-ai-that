import joblib
from const.const import GENERATED_MODEL_PATH

model = joblib.load(GENERATED_MODEL_PATH)

class Classification:
    def __init__(self):
        pass

    def predict_sentiment(text: str) -> str:
        return model.predict([text])[0]