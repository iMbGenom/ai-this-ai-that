# Import joblib, used to laod & saev Python obj (like ML models)
import joblib
from const.const import GENERATED_MODEL_PATH

# Load the model : After saved & trained (joblib.dump())
model = joblib.load(GENERATED_MODEL_PATH)

class Classification:
    def __init__(self):
        pass

    def predict_sentiment(text: str) -> str:
        return model.predict([text])[0]