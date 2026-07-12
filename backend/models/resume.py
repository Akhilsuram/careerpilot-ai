from datetime import datetime
from enum import Enum
import uuid

from sqlalchemy import DateTime, Enum as SQLEnum, String, Text
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import Base


class ResumeStatus(str, Enum):
    UPLOADED = "uploaded"
    PARSING = "parsing"
    PARSED = "parsed"
    FAILED = "failed"


class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    content_hash: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False
    )

    extracted_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    parsed_json: Mapped[dict] = mapped_column(
        JSON,
        nullable=True
    )

    status: Mapped[ResumeStatus] = mapped_column(
        SQLEnum(ResumeStatus),
        default=ResumeStatus.UPLOADED,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )