from dependency_injector import containers, providers

from core.config import Configs
from repository import *
from usecase import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "api.v1.handlers.classification"
        ]
    )


    classification_repository = providers.Factory(ClassificationRepository)

    classification_usecase = providers.Factory(ClassificationUsecase, classification_repository=classification_repository)
