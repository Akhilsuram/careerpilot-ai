from fastapi import APIRouter

from backend.schemas.resume_optimizer import (
    ResumeOptimizerRequest,
)
from backend.use_cases.optimize_resume_use_case import (
    OptimizeResumeUseCase,
)

router = APIRouter(
    prefix="/resume-optimizer",
    tags=["Resume Optimizer"],
)


@router.post("/optimize")
async def optimize_resume(
    request: ResumeOptimizerRequest,
):

    use_case = OptimizeResumeUseCase()

    return use_case.execute(
        request.resume_data,
        request.target_role,
    )