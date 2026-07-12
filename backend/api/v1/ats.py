from fastapi import APIRouter

from backend.schemas.ats import ATSRequest
from backend.use_cases.analyze_ats_use_case import AnalyzeATSUseCase

router = APIRouter(
    prefix="/ats",
    tags=["ATS"],
)


@router.post("/analyze")
async def analyze_ats(
    request: ATSRequest,
):

    use_case = AnalyzeATSUseCase()

    result = use_case.execute(
        request.resume_data,
        request.job_description,
    )

    return result