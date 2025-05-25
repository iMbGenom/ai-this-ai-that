from fastapi import APIRouter
from api.v1.handlers.sentiment import sentiment as sentiment_router

v1_routers = APIRouter()
router_list = [sentiment_router]

for router in router_list:
    v1_routers.include_router(router)