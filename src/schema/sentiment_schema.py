from pydantic import BaseModel

class SentimentPredictRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    prediction: str