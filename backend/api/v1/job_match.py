from fastapi import APIRouter

from backend.schemas.job_match import JobMatchRequest
from backend.use_cases.job_match_use_case import JobMatchUseCase

router = APIRouter(
    prefix="/job-match",
    tags=["Job Match"],
)


@router.post("/search")
async def search_jobs(
    request: JobMatchRequest,
):

    use_case = JobMatchUseCase()

    return use_case.execute(
        request.resume_data,
        request.target_role,
        request.location,
    )