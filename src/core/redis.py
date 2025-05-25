import redis
from core.config import Configs

redis_client = redis.Redis(host=Configs.REDIS_HOST, port=Configs.REDIS_PORT, db=Configs.REDIS_DB, decode_responses=True)