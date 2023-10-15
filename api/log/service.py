from datetime import datetime, UTC

from sqlalchemy import desc, and_
from sqlalchemy.orm import Session

from api.database.schema.log import Log
from api.database.schema.user import User


def get_newest_log(session: Session, user: User) -> Log | None:
    log = (
        session.query(Log)
        .filter(Log.user_id == user.id)
        .order_by(desc(Log.start_timestamp))  # actually not needed
        .first()
    )
    return log


def stamp_in_out(session: Session, user: User) -> dict:
    log = get_newest_log(session, user)

    if log.end_timestamp is None:
        log.end_timestamp = datetime.now(UTC)
        session.add(log)
        session.commit()
        return {
            "status": "success",
            "message": f"Have a great day {user.first_name}!",
            "start_timestamp": log.start_timestamp,
            "end_timestamp": log.end_timestamp
        }
    else:
        log = Log(user_id=user.id, start_timestamp=datetime.now(UTC))
        session.add(log)
        session.commit()
        return {
            "status": "success",
            "message": f"Enjoy your work {user.first_name}!",
            "start_timestamp": log.start_timestamp,
            "end_timestamp": None
        }