from pydantic import BaseModel


class InterviewRequest(BaseModel):
    resume_data: dict
    target_role: str
    job_description: str | None = None


class InterviewQuestion(BaseModel):
    category: str
    difficulty: str
    question: str
    answer: str


class InterviewResponse(BaseModel):
    success: bool
    message: str
    questions: list[InterviewQuestion]