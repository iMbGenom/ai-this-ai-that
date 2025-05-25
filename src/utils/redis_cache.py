from core.redis import redis_client
from const.const import CACHE_TTL_PREDICTION
import hashlib
import json

def get_cache_key(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def get_cached_prediction(text: str) -> str:
    return redis_client.get(get_cache_key(text))

def set_cached_prediction(text: str, result: dict):
    redis_client.set(get_cache_key(text), json.dumps(result), CACHE_TTL_PREDICTION)