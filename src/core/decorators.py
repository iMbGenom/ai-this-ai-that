from functools import wraps
from core.config import Configs
from utils.logger import get_logger
logger = get_logger(__name__)

def redis_enabled(default_return=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info("ENV Config REDIS_ENABLE: %s", Configs.REDIS_ENABLE)
            if not Configs.REDIS_ENABLE:
                return default_return
            return func(*args, **kwargs)
        return wrapper
    return decorator
