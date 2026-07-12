from pydantic import BaseModel


class JobMatchRequest(BaseModel):
    resume_data: dict
    target_role: str
    location: str


class Job(BaseModel):
    company: str
    role: str
    location: str
    match_score: int
    required_skills: list[str]
    missing_skills: list[str]
    reason: str


class JobMatchResponse(BaseModel):
    success: bool
    message: str
    jobs: list[Job]