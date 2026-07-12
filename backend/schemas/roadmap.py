from pydantic import BaseModel


class RoadmapRequest(BaseModel):
    resume_data: dict
    target_role: str


class RoadmapWeek(BaseModel):
    week: int
    topics: list[str]
    goals: list[str]


class RoadmapResponse(BaseModel):
    success: bool
    message: str
    estimated_duration: str
    roadmap: list[RoadmapWeek]