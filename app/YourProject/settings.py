import os
from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "YourProject"
    API_KEY: SecretStr = os.environ.get("API_KEY")
    PROD_MODE: bool | None = os.environ.get("PROD", False)
    DOC_URL: str | None = None
    REDOC_URL: str | None = None
    OPENAPI_URL: str | None = None
    if not PROD_MODE:
        DOC_URL = "/docs"
        REDOC_URL = "/redoc"
        OPENAPI_URL = "/openapi.json"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
