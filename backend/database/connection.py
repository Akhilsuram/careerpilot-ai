import sqlite3

from backend.core.config import DATABASE_URL

DB_PATH = DATABASE_URL.replace("sqlite:///", "")

connection = sqlite3.connect(DB_PATH)