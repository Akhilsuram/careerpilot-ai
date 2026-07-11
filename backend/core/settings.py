from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    # ----------------------------
    # Application
    # ----------------------------
    APP_NAME: str = "CareerPilot AI"
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    # ----------------------------
    # Database
    # ----------------------------
    DATABASE_URL: str

    # ----------------------------
    # LLM Configuration
    # ----------------------------
    LLM_PROVIDER: str = "groq"
    DEFAULT_MODEL: str

    # ----------------------------
    # API Keys
    # ----------------------------
    GROQ_API_KEY: str = ""

    GEMINI_API_KEY: str = ""

    OPENROUTER_API_KEY: str = ""

    OPENAI_API_KEY: str = ""

    # ----------------------------
    # Application
    # ----------------------------
    APP_NAME: str = "CareerPilot AI"
    APP_VERSION: str = "1.0.0"

    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    # ----------------------------
    # Database
    # ----------------------------
    DATABASE_URL: str

    # ----------------------------
    # LLM
    # ----------------------------
    LLM_PROVIDER: str = "groq"
    DEFAULT_MODEL: str

    GROQ_API_KEY: str = ""
    GEMINI_API_KEY: str = ""
    OPENROUTER_API_KEY: str = ""
    OPENAI_API_KEY: str = ""

    # ----------------------------
    # Upload
    # ----------------------------
    MAX_UPLOAD_SIZE: int = 10
    SUPPORTED_FILE_TYPES: str = "pdf"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()