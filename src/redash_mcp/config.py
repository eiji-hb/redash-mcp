"""Configuration for Redash MCP Server."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for Redash MCP Server."""

    url: str
    api_key: str
    timeout: int = 30000  # milliseconds
    max_results: int = 1000
    verify_ssl: bool = True

    model_config = {"env_prefix": "REDASH_", "env_file": ".env"}


def get_settings() -> Settings:
    """Get settings from environment variables."""
    return Settings()
