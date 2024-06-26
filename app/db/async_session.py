from typing import Annotated
from fastapi import Depends
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.config.settings import settings


meta = MetaData()
engine = create_async_engine(settings.ASYNC_DB_URL)
async_session = async_sessionmaker(engine, autoflush=False, autocommit=False, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all)

    db = async_session()
    try:
        yield db
    finally:
        await db.close()


DB = Annotated[AsyncSession, Depends(get_db)]
