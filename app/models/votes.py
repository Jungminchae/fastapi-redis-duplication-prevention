from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column
from app.models.base import Base


class Vote(Base):
    __tablename__ = "votes"

    id = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = mapped_column(Integer)
    candidate_id = mapped_column(Integer)
