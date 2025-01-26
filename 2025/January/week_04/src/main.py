from config.settings import Settings
from services.base_service import BaseService
import logging

logger = logging.getLogger(__name__)

def main():
    try:
        settings = Settings()
        logger.info("Application started")
    except Exception as e:
        logger.error(f"Error starting application: {e}")
        raise

if __name__ == "__main__":
    main()