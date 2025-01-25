from typing import Dict
import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        load_dotenv()
        self.config: Dict = {
            "environment": os.getenv("ENVIRONMENT", "development"),
            "api_key": os.getenv("API_KEY", ""),
            "debug": os.getenv("DEBUG", "False").lower() == "true"
        }

    def get(self, key: str, default=None):
        return self.config.get(key, default)