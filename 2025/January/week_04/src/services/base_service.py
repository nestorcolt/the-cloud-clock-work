from typing import Dict, Any

class BaseService:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def initialize(self) -> None:
        pass