import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def safe_operation(operation: callable, *args, **kwargs) -> Optional[Any]:
    try:
        return operation(*args, **kwargs)
    except Exception as e:
        logger.error(f"Operation failed: {str(e)}")
        return None