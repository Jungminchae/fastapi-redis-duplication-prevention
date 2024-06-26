from pydantic import BaseModel, model_validator


class VoteRequest(BaseModel):
    user_id: int
    candidate_id: int
    token: str | None = None

    @model_validator(mode="before")
    @classmethod
    def validate_token(cls, values: dict) -> dict:
        values["token"] = f"vote_lock:{values['user_id']}:{values['candidate_id']}"

        return values
