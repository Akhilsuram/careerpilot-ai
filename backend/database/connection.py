from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.settings import settings

# Create database directory if it doesn't exist
db_dir = Path("storage/database")
db_dir.mkdir(parents=True, exist_ok=True)

engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()