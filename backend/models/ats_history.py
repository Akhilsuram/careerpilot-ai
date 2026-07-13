from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer

from backend.database.base import Base


class ATSHistory(Base):

    __tablename__ = "ats_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    resume_id = Column(
        Integer,
        nullable=False,
    )

    score = Column(
        Float,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )