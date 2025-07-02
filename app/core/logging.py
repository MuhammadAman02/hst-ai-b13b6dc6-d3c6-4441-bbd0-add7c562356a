"""
Logging configuration for the GenAI Portfolio application.
Provides structured logging with file and console output.
"""

import logging
import sys
import os
from pathlib import Path
from logging.handlers import RotatingFileHandler
from typing import Optional, Dict, Any
from datetime import datetime

# Define what this module exports
__all__ = ["app_logger", "get_logger", "log_structured", "setup_logging"]

# Configure basic logging format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Create application logger
app_logger = logging.getLogger("portfolio")

def setup_logging(
    log_level: str = "INFO",
    log_file: Optional[str] = None,
    max_file_size: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5
) -> None:
    """Setup logging configuration for the application.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Path to log file (optional)
        max_file_size: Maximum size of log file before rotation
        backup_count: Number of backup files to keep
    """
    # Clear any existing handlers
    app_logger.handlers.clear()
    
    # Set log level
    try:
        level = getattr(logging, log_level.upper())
        app_logger.setLevel(level)
    except AttributeError:
        app_logger.setLevel(logging.INFO)
        app_logger.warning(f"Invalid log level '{log_level}', using INFO")
    
    # Create formatter
    formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    app_logger.addHandler(console_handler)
    
    # File handler (if log file is specified)
    if log_file:
        try:
            # Create log directory if it doesn't exist
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Create rotating file handler
            file_handler = RotatingFileHandler(
                log_file,
                maxBytes=max_file_size,
                backupCount=backup_count,
                encoding='utf-8'
            )
            file_handler.setFormatter(formatter)
            app_logger.addHandler(file_handler)
            
            app_logger.info(f"Logging to file: {log_file}")
            
        except Exception as e:
            app_logger.error(f"Failed to setup file logging: {e}")
    
    # Prevent propagation to root logger
    app_logger.propagate = False
    
    app_logger.info(f"Logging initialized with level: {log_level}")

def get_logger(name: str, level: Optional[str] = None) -> logging.Logger:
    """Create a logger for a specific module.
    
    Args:
        name: The name of the module (typically __name__)
        level: Optional log level override
        
    Returns:
        A configured logger instance
    """
    logger = logging.getLogger(f"portfolio.{name}")
    
    # Set level from parameter or inherit from app_logger
    if level:
        try:
            logger.setLevel(getattr(logging, level.upper()))
        except AttributeError:
            logger.setLevel(app_logger.level)
    else:
        logger.setLevel(app_logger.level)
    
    # Add handlers if not already present
    if not logger.handlers:
        # Copy handlers from app_logger
        for handler in app_logger.handlers:
            logger.addHandler(handler)
    
    # Prevent propagation to avoid duplicate logs
    logger.propagate = False
    
    return logger

def log_structured(
    logger: logging.Logger, 
    level: str, 
    message: str, 
    **kwargs: Any
) -> None:
    """Log a message with structured data.
    
    Args:
        logger: The logger instance
        level: The log level (debug, info, warning, error, critical)
        message: The log message
        **kwargs: Additional structured data to include
    """
    try:
        # Create structured log entry
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "message": message,
            **kwargs
        }
        
        # Get the appropriate log method
        log_method = getattr(logger, level.lower(), logger.info)
        
        # Format the structured data
        if kwargs:
            structured_info = " | ".join([f"{k}={v}" for k, v in kwargs.items()])
            full_message = f"{message} | {structured_info}"
        else:
            full_message = message
        
        # Log the message
        log_method(full_message)
        
    except Exception as e:
        # Fallback to simple logging if structured logging fails
        logger.error(f"Structured logging failed: {e}")
        logger.error(f"Original message: {message}")

# Initialize logging with default settings
def _initialize_default_logging():
    """Initialize logging with default settings."""
    try:
        from app.core.config import settings
        setup_logging(
            log_level=settings.LOG_LEVEL,
            log_file=settings.LOG_FILE
        )
    except ImportError:
        # Fallback if settings are not available
        setup_logging(
            log_level=os.getenv("LOG_LEVEL", "INFO"),
            log_file=os.getenv("LOG_FILE")
        )

# Initialize logging when module is imported
_initialize_default_logging()