from typing import Protocol

class RepositoryProtocol(Protocol):
    pass

class BaseUsecase:
    def __init__(self, repository: RepositoryProtocol) -> None:
        self._repository = repository
