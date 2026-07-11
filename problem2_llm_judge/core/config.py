# Application configuration for Problem 2.
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Gemini
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-3.1-flash-lite"

    # Logging
    LOG_LEVEL: str = "INFO"

    # Judge configuration
    MAX_RETRIES: int = 2
    TEMPERATURE: float = 0.0

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    # Returns a cached Settings instance.

    # Using lru_cache ensures that environment variables are read only once during the application lifecycle.
    return Settings()