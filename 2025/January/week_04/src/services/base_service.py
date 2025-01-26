from abc import ABC, abstractmethod
from typing import Any

class BaseService(ABC):
    @abstractmethod
    def process(self) -> Any:
        pass