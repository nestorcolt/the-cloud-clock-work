import logging
from src.config.config import load_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        config = load_config()
        logger.info("Application initialized with configuration")
    except Exception as e:
        logger.error(f"Failed to initialize application: {e}")
        raise

if __name__ == "__main__":
    main()