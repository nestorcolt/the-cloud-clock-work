from typing import Optional
import logging
from langchain import CodeAssistant

logger = logging.getLogger(__name__)

class AICodeGenerator:
    def __init__(self, model: str = "gpt-4"):
        self.assistant = CodeAssistant(model=model)
    
    async def generate_code(self, prompt: str) -> Optional[str]:
        try:
            return await self.assistant.generate(prompt)
        except Exception as e:
            logger.error(f"Code generation failed: {e}")
            return None