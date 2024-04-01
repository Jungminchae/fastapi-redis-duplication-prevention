from fastapi_mctools.cache.redis import RedisCache as Redis


async def get_redis() -> Redis:
    redis = Redis("redis://redis:6379/0")
    return redis.redis
