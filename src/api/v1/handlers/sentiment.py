from fastapi import APIRouter
from schema.sentiment_schema import SentimentPredictRequest, PredictionResponse
from model.model import predict_sentiment
from utils.redis_cache import get_cache_key, get_cached_prediction, set_cached_prediction
import json

sentiment = APIRouter(
    prefix="/sentiment",
    tags=["sentiment"]
)

@sentiment.post("/predict", response_model=PredictionResponse)
async def predict(input: SentimentPredictRequest):
    cache_key = get_cache_key(input.text)
    cached = get_cached_prediction(cache_key)
    if cached:
        return {"prediction": json.loads(cached), "cached": True}
    
    sentiment = predict_sentiment(input.text)
    set_cached_prediction(cache_key, sentiment)
    return {"prediction": sentiment, "cached": False}