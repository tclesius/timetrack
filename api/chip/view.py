from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.auth.service import get_current_user
from api.chip.service import generate_unique_pairing_token, get_chip_by_sn, get_chip_by_token
from api.database.schema.chip import Chip
from api.database.schema.user import User
from api.database.session import get_session

router = APIRouter(prefix="/chip")


@router.get("/pairing-token")
def get_pairing_token(sn: int,
                      session: Annotated[Session, Depends(get_session)]):
    # check if sn is already paired with user
    if chip := get_chip_by_sn(session, sn):
        if chip.user_id is not None:
            return {'token': chip.pairing_token, 'paired': True}
        return {'token': chip.pairing_token, 'paired': False}

    chip = Chip(
        pairing_token=generate_unique_pairing_token(session),
        sn=sn
    )
    session.add(chip)
    session.commit()
    return {'token': chip.pairing_token, 'paired': False}


@router.post("/pairing-token")
def claim_pairing_token(pairing_token: str,
                        user: Annotated[User, Depends(get_current_user)],
                        session: Annotated[Session, Depends(get_session)]):
    if chip := get_chip_by_token(session, pairing_token):
        chip.user_id = user.id
        session.commit()
        return {'message': 'Chip successfully paired with your account.'}
    return {'message': 'Invalid pairing token.'}
