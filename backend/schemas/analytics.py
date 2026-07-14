from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    total_reports: int
    average_ats_score: float
    highest_ats_score: float
    total_resume_versions: int
    total_interview_sessions: int