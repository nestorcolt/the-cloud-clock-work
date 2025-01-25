from typing import Dict
from config.settings import Settings

class ServiceManager:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.services: Dict = {}

    def initialize(self):
        pass