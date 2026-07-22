from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.models.dashboard_metrics import DashboardMetrics


class DashboardRepository:

    def __init__(self):
        self.db: Session = SessionLocal()

        # Ensure one row always exists
        metrics = self.db.query(DashboardMetrics).filter(
            DashboardMetrics.id == 1
        ).first()

        if not metrics:
            metrics = DashboardMetrics(id=1)
            self.db.add(metrics)
            self.db.commit()

    def get_metrics(self):

        return self.db.query(DashboardMetrics).filter(
            DashboardMetrics.id == 1
        ).first()

    def update_ats_score(self, score: int):

        metrics = self.get_metrics()

        metrics.ats_score = score

        self.db.commit()

    def update_resume_score(self, score: int):

        metrics = self.get_metrics()

        metrics.resume_score = score

        self.db.commit()

    def update_interview_questions(self, count: int):

        metrics = self.get_metrics()

        metrics.interview_questions = count

        self.db.commit()

    def update_job_matches(self, count: int):

        metrics = self.get_metrics()

        metrics.job_matches = count

        self.db.commit()