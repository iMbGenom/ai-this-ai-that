from fastapi import APIRouter
from core.middleware import inject
from dependency_injector.wiring import Provide
from core.container import Container
from schema.classification_schema import SentimentPredictRequest, SentimentPredictResponse
from usecase.classification_usecase import ClassificationUsecase
from utils.logger import get_logger
logger = get_logger(__name__)

classification = APIRouter(
    prefix="/classification",
    tags=["classification"]
)
usecase = ClassificationUsecase()

@classification.post("/sentiment-predict", response_model=SentimentPredictResponse)
# @inject
async def predict_sentiment(payload: SentimentPredictRequest):
    logger.info("Received payload: %s", payload)
    # todo: use base handler JSONResponse (from fastapi.responses import JSONResponse)
    return usecase.predict(payload)