from fastapi import APIRouter
from api.v1.handlers.classification_handler import classification as classification_router

v1_routers = APIRouter()
router_list = [classification_router]

for router in router_list:
    v1_routers.include_router(router)