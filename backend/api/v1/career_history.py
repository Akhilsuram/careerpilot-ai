from fastapi import APIRouter

from backend.use_cases.career_history_use_case import CareerHistoryUseCase

router = APIRouter(
    prefix="/career-history",
    tags=["Career History"],
)


@router.get("/")
async def get_history():

    use_case = CareerHistoryUseCase()

    return use_case.execute()