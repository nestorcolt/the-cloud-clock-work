from typing import List, Pattern
import re

class SecurityScanner:
    def __init__(self):
        self.vulnerability_patterns: List[Pattern] = []
    
    def scan(self, code: str) -> bool:
        return all(not pattern.search(code) for pattern in self.vulnerability_patterns)