"""
GenAI Engineer Portfolio - Main Application Entry Point
A professional portfolio showcasing Generative AI expertise with live demos.
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path
from dotenv import load_dotenv
from nicegui import ui

# Verify critical dependencies
def verify_module_installed(module_name):
    """Verify that a Python module is installed."""
    return importlib.util.find_spec(module_name) is not None

def check_dependencies():
    """Check for required dependencies."""
    critical_modules = ["nicegui", "fastapi", "pydantic", "openai", "requests"]
    missing_modules = []
    
    for module in critical_modules:
        if not verify_module_installed(module):
            missing_modules.append(module)
    
    if missing_modules:
        print("ERROR: The following required modules are missing:")
        for module in missing_modules:
            print(f"  - {module}")
        print("\nPlease install dependencies with: pip install -r requirements.txt")
        sys.exit(1)

# Check dependencies before proceeding
check_dependencies()

# Load environment variables
load_dotenv()

# Import the portfolio application
try:
    from app.main import create_portfolio_app
    from app.core.config import settings
    from app.core.logging import app_logger
except ImportError as e:
    print(f"Error importing portfolio application: {e}")
    sys.exit(1)

if __name__ in {"__main__", "__mp_main__"}:
    try:
        # Create and configure the portfolio
        app = create_portfolio_app()
        
        app_logger.info(f"Starting GenAI Portfolio at {settings.HOST}:{settings.PORT}")
        
        # Run the application
        ui.run(
            host=settings.HOST,
            port=settings.PORT,
            title="GenAI Engineer Portfolio",
            favicon="🤖",
            dark=False,
            reload=settings.DEBUG,
            storage_secret=settings.SECRET_KEY,
        )
        
    except Exception as e:
        print(f"Error starting portfolio: {e}")
        sys.exit(1)