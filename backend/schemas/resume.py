from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# ----------------------------------------
# Upload Response
# ----------------------------------------

class ResumeUploadResponse(BaseModel):
    success: bool
    message: str
    resume_id: str


# ----------------------------------------
# Nested Models
# ----------------------------------------

class Education(BaseModel):
    degree: str | None = None
    institution: str | None = None
    duration: str | None = None
    cgpa: str | None = None


class Experience(BaseModel):
    role: str | None = None
    company: str | None = None
    duration: str | None = None
    responsibilities: list[str] = Field(default_factory=list)


class Project(BaseModel):
    name: str | None = None
    technologies: list[str] = Field(default_factory=list)
    description: list[str] = Field(default_factory=list)


class Certification(BaseModel):
    name: str | None = None
    year: str | None = None


# ----------------------------------------
# Resume Data
# ----------------------------------------

class ResumeData(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    summary: str | None = None

    skills: list[str] = Field(default_factory=list)

    education: list[Education] = Field(default_factory=list)

    experience: list[Experience] = Field(default_factory=list)

    projects: list[Project] = Field(default_factory=list)

    certifications: list[Certification] = Field(default_factory=list)


# ----------------------------------------
# Resume Analysis Response
# ----------------------------------------

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