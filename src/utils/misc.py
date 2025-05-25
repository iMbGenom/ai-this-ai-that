import os

def str_to_bool(value: str) -> bool:
    return str(value).lower() in ("true", "1", "yes", "on")