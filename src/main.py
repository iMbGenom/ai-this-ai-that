from fastapi import FastAPI
from utils.class_object import singleton
from utils.date import get_now_utc
from datetime import datetime, timezone
from api.v1.routes import v1_routers
from core.config import Configs
import logging
logging.basicConfig(level=logging.INFO)

@singleton
class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title="Ai This, Ai That, Holy BatChest",
            version="0.0.1"
        )

        @self.app.get("/")
        def root():
            return {"timestamp": get_now_utc()}
        
        self.app.include_router(v1_routers, prefix=Configs.API_V1_STR)

app_creator = AppCreator()
app = app_creator.app