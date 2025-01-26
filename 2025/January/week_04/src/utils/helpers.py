from typing import Any
import logging

logger = logging.getLogger(__name__)

def safe_operation(func: callable) -> Any:
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper