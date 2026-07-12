from fastapi import APIRouter

from backend.schemas.interview import InterviewRequest
from backend.use_cases.interview_use_case import InterviewUseCase

router = APIRouter(
    prefix="/interview",
    tags=["Interview"],
)


@router.post("/generate")
async def generate_questions(
    request: InterviewRequest,
):

    use_case = InterviewUseCase()

    return use_case.execute(
        request.resume_data,
        request.target_role,
        request.job_description,
    )