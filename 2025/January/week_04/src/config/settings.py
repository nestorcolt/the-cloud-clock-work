from typing import Dict
import json
import os

class Settings:
    def __init__(self):
        self.config: Dict = self._load_config()
        
    def _load_config(self) -> Dict:
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        with open(config_path, 'r') as f:
            return json.load(f)
            
    def get(self, key: str, default=None):
        return self.config.get(key, default)