from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)


@router.post("/analyze")
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

        result = service.execute(str(file_path))

        return {
            "success": True,
            "message": "Resume analyzed successfully.",
            "data": result,
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )