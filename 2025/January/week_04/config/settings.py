import os
from pathlib import Path
from typing import Dict

def load_config() -> Dict:
    return {
        "AI_MODEL": os.getenv("AI_MODEL", "gpt-4"),
        "SECURITY_LEVEL": os.getenv("SECURITY_LEVEL", "high"),
        "API_KEY": os.getenv("API_KEY"),
    }