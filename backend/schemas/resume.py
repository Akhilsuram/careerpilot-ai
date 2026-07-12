from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, EmailStr


class ResumeUploadResponse(BaseModel):
    success: bool
    message: str
    resume_id: str


class ResumeData(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    summary: str | None = None

    skills: list[str] = []
    education: list[dict[str, Any]] = []
    experience: list[dict[str, Any]] = []
    projects: list[dict[str, Any]] = []
    certifications: list[str] = []


class ResumeAnalysisResponse(BaseModel):
    success: bool
    message: str

    resume_id: str

    status: str

    provider: str

    model: str

    processing_time: float

    created_at: datetime

    data: ResumeData

    model_config = ConfigDict(from_attributes=True)