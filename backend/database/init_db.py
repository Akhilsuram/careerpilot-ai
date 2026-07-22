from backend.database.base import Base
from backend.database.connection import engine

# Import ALL models so SQLAlchemy registers them
from backend.models.resume import Resume
from backend.models.dashboard_metrics import DashboardMetrics
from backend.models.career_history import CareerHistory
from backend.models.ats_history import ATSHistory


def init_database():
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully.")


if __name__ == "__main__":
    init_database()