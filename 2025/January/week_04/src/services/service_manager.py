from typing import Dict
from config.settings import Settings

class ServiceManager:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.services = {}

    def register_service(self, name: str, service: object):
        self.services[name] = service

    def get_service(self, name: str) -> object:
        return self.services.get(name)