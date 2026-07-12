from fastapi import FastAPI

from backend.api.health import router as health_router
from backend.api.v1.resume import router as resume_router

from backend.api.v1.ats import router as ats_router

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