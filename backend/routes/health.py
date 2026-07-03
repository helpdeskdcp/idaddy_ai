from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "application": "IDaddy AI",
        "version": "0.1.0",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
