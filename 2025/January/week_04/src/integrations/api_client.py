import requests
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        
    def make_request(self, endpoint: str, method: str = "GET", data: Dict = None) -> Any:
        try:
            response = requests.request(
                method=method,
                url=f"{self.base_url}/{endpoint}",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json=data
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"API request failed: {e}")
            raise