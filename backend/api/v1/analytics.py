from fastapi import APIRouter

from backend.use_cases.analytics_use_case import AnalyticsUseCase

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/")
async def analytics():

    return AnalyticsUseCase().execute()