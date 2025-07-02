"""Logging configuration for the portfolio application."""

import logging
import sys
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Create application logger
app_logger = logging.getLogger("portfolio")

def get_logger(name: str) -> logging.Logger:
    """Get a logger with the given name."""
    return logging.getLogger(f"portfolio.{name}")

def log_structured(logger: logging.Logger, level: str, message: str, data: Dict[str, Any]) -> None:
    """Log a structured message with additional data."""
    log_method = getattr(logger, level.lower(), logger.info)
    log_method(f"{message} - {data}")

__all__ = ["app_logger", "get_logger", "log_structured"]