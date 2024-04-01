from pydantic import BaseModel


class VoteRequest(BaseModel):
    user_id: int
    candidate_id: int
