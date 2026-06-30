from fastapi import APIRouter
from app.core.qdrant import client

router = APIRouter(prefix="/system", tags=["System"])

@router.get("/qdrant")
def qdrant_status():
    collections = client.get_collections()
    return {
        "status": "connected",
        "collections": len(collections.collections),
    }