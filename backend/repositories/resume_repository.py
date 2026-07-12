from sqlalchemy.orm import Session

from backend.models.resume import Resume


class ResumeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, resume: Resume) -> Resume:
        self.db.add(resume)
        self.db.commit()
        self.db.refresh(resume)
        return resume

    def get_by_id(self, resume_id: str) -> Resume | None:
        return (
            self.db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

    def get_by_hash(self, content_hash: str) -> Resume | None:
        return (
            self.db.query(Resume)
            .filter(Resume.content_hash == content_hash)
            .first()
        )

    def update(self, resume: Resume) -> Resume:
        self.db.commit()
        self.db.refresh(resume)
        return resume