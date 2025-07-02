"""
Core module for the GenAI Portfolio application.
Provides centralized configuration, logging, and utilities.
"""

from typing import Dict, Any, List, Optional
import logging
import os
import sys
import importlib
from pathlib import Path

# Define what this module exports
__all__ = [
    "app_logger", 
    "get_logger", 
    "log_structured",
    "settings",
    "safe_import",
    "verify_module_exports"
]

# Setup basic logging for initialization
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr
)

# Create fallback logger
fallback_logger = logging.getLogger("portfolio")

def safe_import(module_path: str, attributes: List[str], fallbacks: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Safely import attributes from a module with fallbacks.
    
    Args:
        module_path: The dotted path to the module
        attributes: List of attribute names to import from the module
        fallbacks: Optional dictionary of fallback implementations for attributes
        
    Returns:
        Dictionary of successfully imported attributes or their fallbacks
    """
    result = {}
    fallbacks = fallbacks or {}
    
    try:
        # Attempt to import the module
        module = importlib.import_module(module_path)
        
        # Check if the module has __all__ defined
        module_all = getattr(module, "__all__", None)
        
        # Import each requested attribute
        for attr in attributes:
            # Verify the attribute is exported (if __all__ is defined)
            if module_all is not None and attr not in module_all:
                fallback_logger.warning(
                    f"Attribute '{attr}' is not in {module_path}.__all__, using fallback"
                )
                result[attr] = fallbacks.get(attr)
                continue
                
            # Try to get the attribute from the module
            if hasattr(module, attr):
                result[attr] = getattr(module, attr)
            else:
                fallback_logger.warning(
                    f"Attribute '{attr}' not found in {module_path}, using fallback"
                )
                result[attr] = fallbacks.get(attr)
                
    except ImportError as e:
        fallback_logger.warning(f"Failed to import {module_path}: {e}, using fallbacks")
        # Use fallbacks for all attributes
        for attr in attributes:
            result[attr] = fallbacks.get(attr)
    except Exception as e:
        fallback_logger.error(f"Unexpected error importing {module_path}: {e}, using fallbacks")
        # Use fallbacks for all attributes
        for attr in attributes:
            result[attr] = fallbacks.get(attr)
            
    return result

def verify_module_exports(module_path: str) -> bool:
    """Verify that a module exports all attributes declared in its __all__.
    
    Args:
        module_path: The dotted path to the module
        
    Returns:
        True if all exports are valid, False otherwise
    """
    try:
        module = importlib.import_module(module_path)
        if not hasattr(module, "__all__"):
            fallback_logger.warning(f"Module {module_path} does not define __all__")
            return False
            
        all_attrs = getattr(module, "__all__")
        for attr in all_attrs:
            if not hasattr(module, attr):
                fallback_logger.error(f"Module {module_path} exports '{attr}' in __all__ but does not define it")
                return False
        return True
    except Exception as e:
        fallback_logger.error(f"Failed to verify exports for {module_path}: {e}")
        return False

# Fallback implementations
def fallback_get_logger(name: str) -> logging.Logger:
    """Fallback implementation for get_logger when the actual module fails to load."""
    logger = logging.getLogger(f"portfolio.{name}")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        ))
        logger.addHandler(handler)
    return logger

def fallback_log_structured(logger: logging.Logger, level: str, message: str, **kwargs: Any) -> None:
    """Fallback implementation for structured logging when the actual module fails to load."""
    if kwargs:
        extra_info = " | ".join([f"{k}={v}" for k, v in kwargs.items()])
        full_message = f"{message} | {extra_info}"
    else:
        full_message = message
    
    log_method = getattr(logger, level.lower(), logger.info)
    log_method(full_message)

# Fallback settings class
class FallbackSettings:
    """Fallback settings when the actual settings module fails to import."""
    def __init__(self):
        self.DEBUG = os.getenv("DEBUG", "False").lower() == "true"
        self.APP_NAME = os.getenv("APP_NAME", "GenAI Portfolio")
        self.APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
        self.HOST = os.getenv("HOST", "0.0.0.0")
        self.PORT = int(os.getenv("PORT", "8080"))
        self.SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
        self.LOG_FILE = os.getenv("LOG_FILE")
        
    def __getattr__(self, name: str) -> None:
        # Return None for any settings not explicitly defined
        fallback_logger.warning(f"Accessing undefined setting: {name}")
        return None

# Import logging components with fallbacks
logging_imports = safe_import("app.core.logging", ["app_logger", "get_logger", "log_structured"], {
    "app_logger": fallback_logger,
    "get_logger": fallback_get_logger,
    "log_structured": fallback_log_structured
})

# Extract imported or fallback components
app_logger = logging_imports["app_logger"]
get_logger = logging_imports["get_logger"]
log_structured = logging_imports["log_structured"]

# Import settings with fallbacks
settings_import = safe_import("app.core.config", ["settings"], {
    "settings": FallbackSettings()
})
settings = settings_import["settings"]

# Log successful initialization
if app_logger != fallback_logger:
    app_logger.info(f"Core module initialized successfully for {settings.APP_NAME}")
else:
    fallback_logger.warning("Using fallback logging implementation")