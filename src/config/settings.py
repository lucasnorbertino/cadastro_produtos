from pathlib import Path

from pydantic.v1 import BaseSettings

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    class Config:
        env_file = f'{PROJECT_ROOT}/.env'

    LOG_PATH: str
    LOG_FILE_NAME: str

    TOKEN_EXPIRE_SECONDS: int
    TOKEN_SECRET_KEY: str

    DATABASE_URL: str

settings = Settings()
settings.LOG_PATH = f'{PROJECT_ROOT}/{settings.LOG_PATH}'
