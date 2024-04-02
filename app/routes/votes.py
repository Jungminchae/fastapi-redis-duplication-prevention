from fastapi import APIRouter, HTTPException
from app.db.async_session import DB
from app.service.redis import GetRedis, acquire_lock, release_lock
from app.orms.votes import vote_orm
from app.schemas.votes import VoteRequest

router = APIRouter()


@router.post("/")
async def create_vote(data: VoteRequest, redis: GetRedis, db: DB):
    async with redis.pipeline(transaction=True) as pipe:
        # Redis를 사용하여 투표 토큰의 상태 확인
        await pipe.get(data.token)
        await pipe.setex(data.token, 1, "processing")
        responses = await pipe.execute()

        token_status = responses[0]

        if token_status:
            raise HTTPException(status_code=400, detail="중복 발생")
        await vote_orm.create(db, user_id=data.user_id, candidate_id=data.candidate_id)

    await redis.delete(data.token)
    return {"detail": "투표 완료"}


@router.post("/distributed-lock/")
async def create_vote_by_distributed_lock(data: VoteRequest, redis: GetRedis, db: DB):
    lock_key = f"vote:{data.token}"
    lock_acquired = await acquire_lock(redis, lock_key, 1)
    if not lock_acquired:
        raise HTTPException(status_code=400, detail="중복 발생")

    try:
        await vote_orm.create(db, user_id=data.user_id, candidate_id=data.candidate_id)
    finally:
        await release_lock(redis, lock_key)
    return {"detail": "투표 완료"}
