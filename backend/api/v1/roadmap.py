from fastapi import APIRouter

from backend.schemas.roadmap import RoadmapRequest
from backend.use_cases.roadmap_use_case import RoadmapUseCase

router = APIRouter(
    prefix="/roadmap",
    tags=["Career Roadmap"],
)


@router.post("/generate")
async def generate_roadmap(
    request: RoadmapRequest,
):

    use_case = RoadmapUseCase()

    return use_case.execute(
        request.resume_data,
        request.target_role,
    )