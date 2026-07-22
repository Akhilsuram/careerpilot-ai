from fastapi import APIRouter

from backend.schemas.career_copilot import CareerCopilotRequest
from backend.services.career_copilot_service import CareerCopilotService

router = APIRouter(
    prefix="/career-copilot",
    tags=["Career Copilot"],
)

service = CareerCopilotService()


@router.post("/run")
async def run(
    request: CareerCopilotRequest,
):

    return service.execute(
        request.resume_data,
        request.target_role,
    )