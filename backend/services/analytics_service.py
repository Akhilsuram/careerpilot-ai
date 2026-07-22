from backend.memory.memory_manager import MemoryManager
from backend.repositories.dashboard_repository import DashboardRepository


class AnalyticsService:

    def __init__(self):
        self.memory = MemoryManager()
        self.dashboard = DashboardRepository()

    def execute(self):

        metrics = self.dashboard.get_metrics()

        career_history = self.memory.get_career_history()
        ats_history = self.memory.get_ats_history()

        scores = [item.score for item in ats_history]

        return {

            # Dashboard Cards
            "ats_score": metrics.ats_score,
            "resume_score": metrics.resume_score,
            "interview_questions": metrics.interview_questions,
            "job_matches": metrics.job_matches,

            # Analytics Page
            "total_reports": len(career_history),
            "average_ats_score": round(sum(scores) / len(scores), 2) if scores else 0,
            "highest_ats_score": max(scores) if scores else 0,
            "total_resume_versions": len(
                {item.resume_id for item in career_history}
            ),
            "total_interview_sessions": metrics.interview_questions,
        }