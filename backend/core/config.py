from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
ENVIRONMENT = os.getenv("ENVIRONMENT")
LOG_LEVEL = os.getenv("LOG_LEVEL")

DATABASE_URL = os.getenv("DATABASE_URL")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")