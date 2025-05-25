import os
from utils.misc import str_to_bool 
from dotenv import load_dotenv
load_dotenv()

ENV: str = ""

class Configs():
    API_V1_STR: str = "/v1"

    ENV: str = os.getenv("ENV", "")

    REDIS_ENABLE: str = str_to_bool(os.getenv("REDIS_ENABLE", "false"))
    REDIS_HOST: str = os.getenv("REDIS_HOST", "")
    REDIS_PORT: str = os.getenv("REDIS_PORT", "")
    REDIS_DB: str = os.getenv("REDIS_DB", "")