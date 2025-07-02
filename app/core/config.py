"""
Configuration settings for the GenAI Portfolio application.
Uses pydantic-settings for environment variable management.
"""

from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict
from typing import Optional, List
import os
from pathlib import Path

class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    # Application
    APP_NAME: str = Field(default="GenAI Engineer Portfolio")
    APP_VERSION: str = Field(default="1.0.0")
    APP_DESCRIPTION: str = Field(default="Professional portfolio showcasing Generative AI expertise")
    DEBUG: bool = Field(default=False)
    
    # Server
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8080)
    
    # Security
    SECRET_KEY: str = Field(default="your-secret-key-change-in-production")
    ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)
    
    # Database
    DATABASE_URL: str = Field(default="sqlite:///./data/portfolio.db")
    
    # AI Services
    OPENAI_API_KEY: Optional[str] = Field(default=None)
    ANTHROPIC_API_KEY: Optional[str] = Field(default=None)
    
    # Email Configuration
    SMTP_HOST: Optional[str] = Field(default=None)
    SMTP_PORT: int = Field(default=587)
    SMTP_USERNAME: Optional[str] = Field(default=None)
    SMTP_PASSWORD: Optional[str] = Field(default=None)
    SMTP_USE_TLS: bool = Field(default=True)
    
    # Contact Information
    CONTACT_EMAIL: str = Field(default="contact@genai-engineer.com")
    LINKEDIN_URL: str = Field(default="https://linkedin.com/in/genai-engineer")
    GITHUB_URL: str = Field(default="https://github.com/genai-engineer")
    
    # File Upload
    MAX_FILE_SIZE: int = Field(default=10 * 1024 * 1024)  # 10MB
    UPLOAD_DIRECTORY: str = Field(default="./uploads")
    ALLOWED_EXTENSIONS: List[str] = Field(default=["pdf", "doc", "docx", "txt"])
    
    # Logging
    LOG_LEVEL: str = Field(default="INFO")
    LOG_FILE: Optional[str] = Field(default="./logs/portfolio.log")
    
    # API Configuration
    API_PREFIX: str = Field(default="/api/v1")
    CORS_ORIGINS: List[str] = Field(default=["*"])
    
    # Rate Limiting
    RATE_LIMIT_REQUESTS: int = Field(default=100)
    RATE_LIMIT_WINDOW: int = Field(default=3600)  # 1 hour
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create necessary directories
        self._create_directories()
    
    def _create_directories(self):
        """Create necessary directories if they don't exist."""
        directories = [
            Path(self.UPLOAD_DIRECTORY),
            Path("./data"),
            Path("./logs"),
            Path("./static"),
            Path("./static/images"),
            Path("./static/css"),
            Path("./static/js")
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    @property
    def database_path(self) -> Path:
        """Get the database file path."""
        if self.DATABASE_URL.startswith("sqlite:///"):
            db_path = self.DATABASE_URL.replace("sqlite:///", "")
            return Path(db_path)
        return Path("./data/portfolio.db")

# Create global settings instance
settings = Settings()

# Validate critical settings
def validate_settings():
    """Validate critical application settings."""
    errors = []
    
    # Check if required directories exist and are writable
    critical_dirs = [
        Path("./data"),
        Path("./logs"),
        Path(settings.UPLOAD_DIRECTORY)
    ]
    
    for directory in critical_dirs:
        if not directory.exists():
            try:
                directory.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                errors.append(f"Cannot create directory {directory}: {e}")
        elif not os.access(directory, os.W_OK):
            errors.append(f"Directory {directory} is not writable")
    
    # Validate AI API keys if AI features are enabled
    if not settings.OPENAI_API_KEY and not settings.ANTHROPIC_API_KEY:
        print("WARNING: No AI API keys configured. AI features will use mock responses.")
    
    # Validate email configuration if contact form is enabled
    if settings.SMTP_HOST and not all([settings.SMTP_USERNAME, settings.SMTP_PASSWORD]):
        print("WARNING: SMTP host configured but missing username/password. Contact form emails may fail.")
    
    if errors:
        raise ValueError(f"Configuration validation failed: {'; '.join(errors)}")

# Validate settings on import
try:
    validate_settings()
except Exception as e:
    print(f"Configuration warning: {e}")