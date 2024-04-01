from fastapi_mctools.orms.sqlalchemy import async_base
from app.models.base import Base
from app.models.votes import Vote


class VoteCreate(async_base.ACreateBase):
    ...


class VoteORM(VoteCreate):
    def __init__(self, model: Base):
        super().__init__(model)


vote_orm = VoteORM(Vote)
