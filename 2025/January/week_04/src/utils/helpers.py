import logging
from typing import Any, Dict

def setup_logging(log_level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def load_json_file(file_path: str) -> Dict[str, Any]:
    import json
    with open(file_path, 'r') as f:
        return json.load(f)