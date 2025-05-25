from fastapi import BackgroundTasks
from model.model import predict_sentiment
from utils.redis_cache import set_cached_prediction

def job_to_analyze_and_cache(background_tasks: BackgroundTasks, cache_key: str, result: str):
    background_tasks.add_task(set_cached_prediction(cache_key, result))
    