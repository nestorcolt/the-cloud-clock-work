from typing import Dict
import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        load_dotenv()
        self.config = self._load_configuration()
    
    def _load_configuration(self) -> Dict[str, str]:
        return {
            "API_KEY": os.getenv("API_KEY", ""),
            "DATABASE_URL": os.getenv("DATABASE_URL", ""),
            "ENVIRONMENT": os.getenv("ENVIRONMENT", "development")
        }