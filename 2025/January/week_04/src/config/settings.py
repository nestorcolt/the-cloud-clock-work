from typing import Dict
import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        load_dotenv()
        self.config = {
            "API_KEY": os.getenv("API_KEY"),
            "DATABASE_URL": os.getenv("DATABASE_URL"),
            "ENVIRONMENT": os.getenv("ENVIRONMENT", "development")
        }

    def get(self, key: str) -> str:
        return self.config.get(key)