from pydantic import BaseModel


class ResumeOptimizerRequest(BaseModel):
    resume_data: dict
    target_role: str


class ResumeOptimizerResponse(BaseModel):
    success: bool
    message: str

    optimized_summary: str
    optimized_skills: list[str]
    optimized_projects: list[dict]
    optimized_experience: list[dict]

    recommendations: list[str]

    strengths: list[str] = []
    improvements: list[str] = []