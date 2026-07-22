from datetime import datetime
from pathlib import Path
import traceback
from backend.utils.resume_normalizer import ResumeNormalizer
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
    # Only PDF files
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF resume only."
        )

    # File name validation
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Invalid file format. Only PDF files are supported."
        )

    # Maximum size (5 MB)
    contents = await file.read()

    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="Resume size must be less than 5 MB."
        )

    await file.seek(0)
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
        parsed = ResumeNormalizer.normalize(parsed)

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

    except HTTPException:
        raise

    except Exception:

        print("\n========== RESUME API ERROR ==========")
        traceback.print_exc()
        print("======================================\n")

        raise HTTPException(
            status_code=500,
            detail="Something went wrong while analyzing your resume. Please try again."
        )