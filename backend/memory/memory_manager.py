from backend.repositories.ats_history_repository import ATSHistoryRepository
from backend.repositories.career_history_repository import CareerHistoryRepository


class MemoryManager:

    def __init__(self):

        self.ats_repository = ATSHistoryRepository()

        self.career_repository = CareerHistoryRepository()

    def save_ats_score(
        self,
        resume_id: int,
        score: float,
    ):

        return self.ats_repository.save(
            resume_id,
            score,
        )

    def save_career_report(
        self,
        resume_id: int,
        goal: str,
        ats_score: str,
        report: dict,
    ):

        return self.career_repository.save(
            resume_id,
            goal,
            ats_score,
            report,
        )

    def get_ats_history(self):

        return self.ats_repository.get_all()

    def get_career_history(self):

        return self.career_repository.get_all()