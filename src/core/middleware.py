from functools import wraps
from dependency_injector.wiring import inject as di_inject
from loguru import logger
from usecase.base_usecase import BaseUsecase

def inject(func):
    @di_inject
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        injected_services = [arg for arg in kwargs.values() if isinstance(arg, BaseUsecase)]
        if len(injected_services) == 0:
            return result
        else:
            try:
                injected_services[-1].close_scoped_session()
            except Exception as e:
                logger.error(e)

        return result

    return wrapper
