from backend.database.base import Base
from backend.database.connection import engine

# Import ALL models here so SQLAlchemy registers them
from backend.models.resume import Resume  # noqa: F401
from backend.models.dashboard_metrics import DashboardMetrics

def init_database():
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully.")


if __name__ == "__main__":
    init_database()