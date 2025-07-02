"""Application configuration using Pydantic settings."""

from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict
from typing import List

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
    APP_DESCRIPTION: str = Field(default="Professional portfolio showcasing Generative AI expertise")
    APP_VERSION: str = Field(default="1.0.0")
    DEBUG: bool = Field(default=False)
    
    # Server
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8080)
    
    # Security
    SECRET_KEY: str = Field(default="your-secret-key-change-in-production")
    
    # AI Services
    OPENAI_API_KEY: str = Field(default="")
    HUGGINGFACE_API_KEY: str = Field(default="")
    
    # Contact
    CONTACT_EMAIL: str = Field(default="contact@genai-engineer.com")
    SMTP_SERVER: str = Field(default="")
    SMTP_PORT: int = Field(default=587)
    SMTP_USERNAME: str = Field(default="")
    SMTP_PASSWORD: str = Field(default="")
    
    # Social Links
    GITHUB_URL: str = Field(default="https://github.com/genai-engineer")
    LINKEDIN_URL: str = Field(default="https://linkedin.com/in/genai-engineer")
    TWITTER_URL: str = Field(default="https://twitter.com/genai_engineer")
    
    # Portfolio Data
    ENGINEER_NAME: str = Field(default="Alex Chen")
    ENGINEER_TITLE: str = Field(default="Senior GenAI Engineer")
    ENGINEER_LOCATION: str = Field(default="San Francisco, CA")
    YEARS_EXPERIENCE: int = Field(default=5)

settings = Settings()