from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_PORT: int = 8080
    APP_HOST: str = '0.0.0.0'
    APP_DEBUG_MODE: bool = False
  
    DATABASE_URL: str = "sqlite+aiosqlite:///./registry.db"
    
    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent.parent / ".env")


settings = Settings()
