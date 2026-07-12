from backend.database.connection import SessionLocal
from backend.models.career_history import CareerHistory


class CareerHistoryRepository:

    def save(
        self,
        resume_id: int,
        goal: str,
        ats_score: str,
        report: dict,
    ):

        db = SessionLocal()

        history = CareerHistory(
            resume_id=resume_id,
            goal=goal,
            ats_score=ats_score,
            report=report,
        )

        db.add(history)

        db.commit()

        db.refresh(history)

        db.close()

        return history

    def get_all(self):

        db = SessionLocal()

        rows = db.query(
            CareerHistory
        ).all()

        db.close()

        return rows