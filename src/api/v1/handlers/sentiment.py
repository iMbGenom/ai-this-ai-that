from fastapi import APIRouter, BackgroundTasks
from schema.sentiment_schema import SentimentPredictRequest, SentimentPredictResponse
from model.model import predict_sentiment
from utils.redis_cache import get_cache_key, get_cached_prediction, set_cached_prediction
import json
from jobs.sentiment_jobs import job_to_analyze_and_cache

sentiment = APIRouter(
    prefix="/sentiment",
    tags=["sentiment"]
)

@sentiment.post("/predict", response_model=SentimentPredictResponse)
async def predict(input: SentimentPredictRequest, background_tasks: BackgroundTasks):
    cache_key = get_cache_key(input.text)
    cached = get_cached_prediction(cache_key)
    if cached:
        decoded = json.loads(cached)
        return SentimentPredictResponse(prediction=decoded, cached=True)
    
    # logic
    result = predict_sentiment(input.text)

    # save redis using jobs
    job_to_analyze_and_cache(background_tasks, cache_key, result)

    # save redis inline
    # set_cached_prediction(cache_key, result)

    return SentimentPredictResponse(prediction=result, cached=False)
    # return {"prediction": result, "cached": False}