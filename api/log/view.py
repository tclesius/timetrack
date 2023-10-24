from datetime import datetime, UTC
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from api.auth.service import get_current_user
from api.database.schema.user import User
from api.database.session import get_session
from api.log.model import PostTrackResponse
from api.log.service import stamp_in_out, get_newest_log

router = APIRouter(prefix='/log')


@router.post("/stampinout", response_model=PostTrackResponse)
async def post_stampinout(session: Annotated[Session, Depends(get_session)],
                          user: Annotated[User, Depends(get_current_user)]):
    return stamp_in_out(session, user)


@router.get("/stats")
async def get_stats(session: Annotated[Session, Depends(get_session)],
                    user: Annotated[User, Depends(get_current_user)]):
    if log := get_newest_log(session, user):
        return {
            "message": "",
            "start_timestamp": log.start_timestamp,
            "end_timestamp": log.end_timestamp
        }
    return {
        "message": "",
        "start_timestamp": None,
        "end_timestamp": None
    }