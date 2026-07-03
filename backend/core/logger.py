"""
Central logging configuration.
"""

import sys
from loguru import logger

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    enqueue=True,
    backtrace=True,
    diagnose=False,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "{name}:{function}:{line} | "
           "{message}",
)
