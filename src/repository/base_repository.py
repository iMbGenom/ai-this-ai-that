from typing import Type, TypeVar
from model.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)

class BaseRepository:
    def __init__(self, model: Type[T]) -> None:
        self.model = model
