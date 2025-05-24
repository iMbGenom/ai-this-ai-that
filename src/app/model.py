# Import joblib, used to laod & saev Python obj (like ML models)
import joblib
from config.config import MODEL_PATH

# Load the model : After saved & trained (joblib.dump())
model = joblib.load(MODEL_PATH)

def predict_sentiment(text: str) -> str:
    # Get the first arr
    return model.predict([text])[0]