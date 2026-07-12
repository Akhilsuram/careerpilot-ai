from backend.database.base import Base
from backend.database.connection import engine

import backend.models.career_history

Base.metadata.create_all(bind=engine)

print("Career History Table Created")