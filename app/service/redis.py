from typing import Annotated
from fastapi import Depends
from redis import asyncio as aioredis
from redis.asyncio import Redis


async def get_redis() -> Redis:
    """Redis 연결"""
    redis = aioredis.from_url("redis://redis:6379/0")
    return redis


async def acquire_lock(redis: Redis, lock_key: str, timeout: int = 1):
    """분산락 획득"""
    lock_acquired = await redis.set(lock_key, "locked", ex=timeout, nx=True)
    return lock_acquired


async def release_lock(redis: Redis, lock_key: str):
    """분산락 해제"""
    await redis.delete(lock_key)


GetRedis = Annotated[Redis, Depends(get_redis)]
