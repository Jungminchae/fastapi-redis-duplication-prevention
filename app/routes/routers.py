from fastapi import APIRouter
from app.routes.votes import router as votes_router

router = APIRouter()
router.include_router(votes_router, prefix="/votes")
