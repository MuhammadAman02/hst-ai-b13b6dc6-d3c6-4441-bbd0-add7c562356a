"""
Main application module for the GenAI Portfolio.
Creates and configures the NiceGUI application with FastAPI integration.
"""

from nicegui import ui, app as nicegui_app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import asyncio
from typing import Optional

from app.core import app_logger, settings
from app.api.router import api_router
from app.ui.pages import create_portfolio_pages
from app.ui.components import setup_theme

def create_fastapi_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    
    # Create FastAPI app
    fastapi_app = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
    )
    
    # Add CORS middleware
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include API router
    fastapi_app.include_router(api_router, prefix=settings.API_PREFIX)
    
    # Mount static files
    static_path = Path("./static")
    if static_path.exists():
        fastapi_app.mount("/static", StaticFiles(directory=static_path), name="static")
    
    # Health check endpoint
    @fastapi_app.get("/health")
    async def health_check():
        return {
            "status": "healthy",
            "app": settings.APP_NAME,
            "version": settings.APP_VERSION
        }
    
    app_logger.info("FastAPI application configured successfully")
    return fastapi_app

def create_portfolio_app() -> FastAPI:
    """Create the complete portfolio application with NiceGUI integration."""
    
    try:
        # Create FastAPI app
        fastapi_app = create_fastapi_app()
        
        # Configure NiceGUI to use our FastAPI app
        nicegui_app.mount_to(fastapi_app)
        
        # Setup theme and styling
        setup_theme()
        
        # Create portfolio pages
        create_portfolio_pages()
        
        app_logger.info("Portfolio application created successfully")
        return fastapi_app
        
    except Exception as e:
        app_logger.error(f"Failed to create portfolio application: {e}")
        raise

# Global app instance
app: Optional[FastAPI] = None

def get_app() -> FastAPI:
    """Get or create the application instance."""
    global app
    if app is None:
        app = create_portfolio_app()
    return app

# Create the app when this module is imported
if __name__ != "__main__":
    try:
        app = create_portfolio_app()
    except Exception as e:
        app_logger.error(f"Failed to initialize application: {e}")
        # Create a minimal FastAPI app as fallback
        app = FastAPI(title="Portfolio (Fallback Mode)")
        
        @app.get("/")
        async def fallback_root():
            return {"message": "Portfolio application is in fallback mode", "error": str(e)}