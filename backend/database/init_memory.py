from backend.database.base import Base
from backend.database.connection import engine

import backend.models.ats_history
import backend.models.career_history

Base.metadata.create_all(bind=engine)

print("Memory Tables Created Successfully")