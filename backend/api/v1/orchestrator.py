from fastapi import APIRouter

from backend.schemas.planner import PlannerRequest
from backend.use_cases.orchestrator_use_case import OrchestratorUseCase

router = APIRouter(
    prefix="/career",
    tags=["Career Copilot"],
)


@router.post("/analyze")
async def analyze_career(
    request: PlannerRequest,
):

    use_case = OrchestratorUseCase()

    return use_case.execute(
        request.resume_data,
        request.user_goal,
    )