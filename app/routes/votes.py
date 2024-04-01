from fastapi import APIRouter

# from app.orms.votes import vote_orm
from app.schemas.votes import VoteRequest

router = APIRouter()


@router.post("/")
async def create_vote(data: VoteRequest):
    ...
