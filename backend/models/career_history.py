from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String

from backend.database.base import Base


class CareerHistory(Base):

    __tablename__ = "career_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    resume_id = Column(
        Integer,
        nullable=False,
    )

    goal = Column(
        String,
        nullable=False,
    )

    ats_score = Column(
        String,
        nullable=True,
    )

    report = Column(
        JSON,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )