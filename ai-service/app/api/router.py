from fastapi import APIRouter

from app.api.health import router as health_router
from app.api.generate import router as generate_router
from app.api.ingest import router as ingest_router

api_router = APIRouter()

api_router.include_router(health_router, tags=["Health"])

api_router.include_router(generate_router, prefix="/generate", tags=["Generation"])

api_router.include_router(ingest_router, prefix="/ingest", tags=["Ingestion"])