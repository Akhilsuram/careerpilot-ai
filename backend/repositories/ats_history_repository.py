from backend.database.connection import SessionLocal
from backend.models.ats_history import ATSHistory


class ATSHistoryRepository:

    def save(
        self,
        resume_id: int,
        score: float,
    ):

        db = SessionLocal()

        history = ATSHistory(
            resume_id=resume_id,
            score=score,
        )

        db.add(history)

        db.commit()

        db.refresh(history)

        db.close()

        return history

    def get_all(self):

        db = SessionLocal()

        rows = db.query(
            ATSHistory
        ).all()

        db.close()

        return rows