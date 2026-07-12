from typing import Any

from pydantic import BaseModel, Field


class ATSRequest(BaseModel):
    resume_data: dict[str, Any]
    job_description: str


class ATSScore(BaseModel):
    overall_score: int = Field(..., ge=0, le=100)

    category_scores: dict[str, int]

    matched_keywords: list[str]

    missing_keywords: list[str]

    strengths: list[str]

    weaknesses: list[str]

    recommendations: list[str]


class ATSResponse(BaseModel):
    success: bool
    message: str
    data: ATSScore