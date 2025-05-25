from model.classification_model import Classification
from repository.base_repository import BaseRepository

class ClassificationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Classification)
