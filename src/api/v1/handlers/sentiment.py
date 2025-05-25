from fastapi import APIRouter
from schema.sentiment_schema import SentimentPredictRequest, PredictionResponse
from model.model import predict_sentiment

sentiment = APIRouter(
    prefix="/sentiment",
    tags=["sentiment"]
)

@sentiment.post("/predict", response_model=PredictionResponse)
async def predict(input: SentimentPredictRequest):
    sentiment = predict_sentiment(input.text)
    return {"prediction": sentiment}