from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from backend.core.settings import settings
from backend.database.connection import get_db
from backend.schemas.resume import ResumeAnalysisResponse, ResumeData
from backend.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)


@router.post(
    "/analyze",
    response_model=ResumeAnalysisResponse,
)
async def analyze_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    try:

        upload_dir = Path("storage/uploads")
        upload_dir.mkdir(parents=True, exist_ok=True)

        file_path = upload_dir / file.filename

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        service = ResumeService(db)

        response = service.execute(str(file_path))

        result = response["data"]

        parsed = result["parsed"]

        resume = result["resume"]

        return ResumeAnalysisResponse(
            success=response["success"],
            message=response["message"],
            resume_id=resume.id,
            status=resume.status.value,
            provider=settings.LLM_PROVIDER,
            model=settings.DEFAULT_MODEL,
            processing_time=response["processing_time"],
            created_at=resume.created_at,
            data=ResumeData(**parsed),
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )