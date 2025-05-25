import logging
import sys

def get_logger(name: str = __name__, level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(levelname)s:[%(asctime)s][%(name)s] %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
