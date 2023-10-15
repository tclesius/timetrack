from datetime import datetime

from pydantic import BaseModel, constr
import secrets


class RFIDToken(BaseModel):
    token: constr(max_length=8, min_length=8)

    @classmethod
    def generate(cls):
        random_token = secrets.token_hex(4)
        return cls(token=random_token)


class PostTrackResponse(BaseModel):
    status: str
    message: str
    start_timestamp: datetime
    end_timestamp: datetime | None
