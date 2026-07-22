from sqlalchemy import Column, Integer

from backend.database.base import Base


class DashboardMetrics(Base):
    __tablename__ = "dashboard_metrics"

    id = Column(Integer, primary_key=True, default=1)

    ats_score = Column(Integer, default=0)

    resume_score = Column(Integer, default=0)

    interview_questions = Column(Integer, default=0)

    job_matches = Column(Integer, default=0)