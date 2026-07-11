from fastapi import APIRouter

from backend.core.settings import settings

router = APIRouter()


@router.get("/")
def root():
    return {
        "success": True,
        "message": "Application Running",
        "data": {
            "app": settings.APP_NAME,
            "status": "running",
        },
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected",
        "provider": settings.LLM_PROVIDER,
        "model": settings.DEFAULT_MODEL,
    }


@router.get("/version")
def version():
    return {
        "version": settings.APP_VERSION,
    }