from typing import Dict
import os
from pathlib import Path

def load_config() -> Dict:
    return {
        "AI_MODEL": os.getenv("AI_MODEL", "gpt-4"),
        "SECURITY_LEVEL": os.getenv("SECURITY_LEVEL", "high"),
        "CI_CD_ENABLED": os.getenv("CI_CD_ENABLED", "true").lower() == "true"
    }