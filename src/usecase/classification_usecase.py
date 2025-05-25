
from schema.classification_schema import SentimentPredictRequest, SentimentPredictResponse
import json
from utils.redis_cache import get_cache_key, get_cached_prediction, set_cached_prediction
from model.classification_model import Classification
from fastapi import BackgroundTasks
from jobs.bg_task_jobs import job_to_analyze_and_cache

class ClassificationUsecase():
    def __init__(self):
        super().__init__()

    def predict(self, schema: SentimentPredictRequest, background_tasks: BackgroundTasks = None) -> SentimentPredictResponse:
        cache_key = get_cache_key(schema.text)
        cached = get_cached_prediction(cache_key)
        if cached:
            decoded = json.loads(cached)
            return SentimentPredictResponse(prediction=decoded, cached=True)

        result = Classification.predict_sentiment(schema.text)

        if background_tasks:
            # save redis using jobs
            job_to_analyze_and_cache(background_tasks, cache_key, result)
        else:
            # save redis inline
            set_cached_prediction(cache_key, result)

        return SentimentPredictResponse(prediction=result, cached=False)