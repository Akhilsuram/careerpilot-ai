from fastapi import FastAPI

from backend.api.health import router as health_router
from backend.api.v1.resume import router as resume_router

from backend.api.v1.ats import router as ats_router
from backend.api.v1.job_match import router as job_match_router
from backend.api.v1.interview import router as interview_router
from backend.api.v1.roadmap import router as roadmap_router
from backend.api.v1.orchestrator import (
    router as orchestrator_router,
)

from backend.api.v1.resume_optimizer import (
    router as resume_optimizer_router,
)

app = FastAPI(
    title="CareerPilot AI",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(resume_router)
app.include_router(ats_router)
app.include_router(
    resume_optimizer_router
)
app.include_router(job_match_router)
app.include_router(interview_router)
app.include_router(roadmap_router)
app.include_router(
    orchestrator_router
)
