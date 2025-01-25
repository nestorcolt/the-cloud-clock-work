from typing import Dict, Any
import os
from dotenv import load_dotenv

def load_config() -> Dict[str, Any]:
    load_dotenv()
    
    return {
        "environment": os.getenv("ENVIRONMENT", "development"),
        "api_key": os.getenv("API_KEY", ""),
        "debug": os.getenv("DEBUG", "False").lower() == "true"
    }