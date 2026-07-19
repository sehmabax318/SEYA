from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "assistant": "SEYA",
        "status": "online",
        "version": "0.1.0",
    }