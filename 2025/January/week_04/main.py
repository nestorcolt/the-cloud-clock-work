import asyncio
import logging
from src.ai_assistant.code_generator import AICodeGenerator
from src.security.scanner import SecurityScanner
from config.settings import load_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    config = load_config()
    code_generator = AICodeGenerator(model=config["AI_MODEL"])
    security_scanner = SecurityScanner()
    
    logger.info("AI-Assisted Development Environment Initialized")

if __name__ == "__main__":
    asyncio.run(main())