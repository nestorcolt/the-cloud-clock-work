from config.settings import Settings
from services.service_manager import ServiceManager
import logging

logger = logging.getLogger(__name__)

def main():
    try:
        settings = Settings()
        service_manager = ServiceManager(settings)
        logger.info("Application initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize application: {e}")
        raise

if __name__ == "__main__":
    main()