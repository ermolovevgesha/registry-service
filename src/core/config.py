from typing import Annotated, Any, Literal
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    AnyUrl,
    BeforeValidator,
    PostgresDsn,
    RedisDsn,
    computed_field,
)


class Settings(BaseSettings):
    APP_PORT: int = 8000
    APP_HOST: str = '0.0.0.0'
    APP_DEBUG_MODE: bool = True
  
    POSTGRES_DB_NAME: str
    POSTGRES_DB_USER: str
    POSTGRES_DB_PASSWORD: str
    POSTGRES_DB_PORT: int
    POSTGRES_DB_HOST: str

  
    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_DB_USER,
            password=self.POSTGRES_DB_PASSWORD,
            host=self.POSTGRES_DB_HOST,
            port=self.POSTGRES_DB_PORT,
            path=self.POSTGRES_DB_NAME,
        )
    
    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent.parent / ".env")


settings = Settings()
