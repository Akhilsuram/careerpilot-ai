from pydantic import BaseModel


class PlannerRequest(BaseModel):
    user_goal: str
    resume_data: dict


class PlannerResponse(BaseModel):
    success: bool
    message: str
    report: dict