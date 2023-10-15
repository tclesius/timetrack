from datetime import datetime, UTC
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from api.auth.service import get_current_user
from api.database.schema.user import User
from api.database.session import get_session
from api.log.model import PostTrackResponse
from api.log.service import stamp_in_out, get_newest_log
from api.user.service import get_user_by_rfid_token

router = APIRouter(prefix='/log')


@router.post("/stamp-web", response_model=PostTrackResponse)
async def post_track_web(session: Annotated[Session, Depends(get_session)],
                         user: Annotated[User, Depends(get_current_user)]):
    return stamp_in_out(session, user)


@router.post("/stamp-rfid", response_model=PostTrackResponse)
async def post_track_rfid(session: Annotated[Session, Depends(get_session)],
                          rfid_token: Annotated[str, Query(min_length=8, max_length=8)] = None):
    user = get_user_by_rfid_token(session, rfid_token)
    return stamp_in_out(session, user)


@router.get("/stats")
async def get_stats(session: Annotated[Session, Depends(get_session)],
                    user: Annotated[User, Depends(get_current_user)]):
    log = get_newest_log(session, user)
    return {
        "status": "success",
        "message": f"",
        "start_timestamp": log.start_timestamp,
        "end_timestamp": log.end_timestamp
    }
