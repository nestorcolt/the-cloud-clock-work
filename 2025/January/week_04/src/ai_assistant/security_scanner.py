from typing import List
import re

class SecurityScanner:
    def __init__(self):
        self.vulnerability_patterns = []
        
    def scan(self, code: str) -> bool:
        for pattern in self.vulnerability_patterns:
            if re.search(pattern, code):
                return False
        return True