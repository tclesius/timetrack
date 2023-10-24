from typing import Annotated

from fastapi import APIRouter, Depends, Query
from pydantic import EmailStr
from sqlalchemy.orm import Session

from api import exceptions
from api.auth.service import get_current_user, get_password_hash
from api.chip.service import get_chip_by_token
from api.database.schema.user import User
from api.database.session import get_session
from api.user.service import get_user_by_email, create_user

router = APIRouter(prefix='/user')


@router.get("/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.post("/register")
async def register_user(email: EmailStr,
                        password: str,
                        first_name: str,
                        last_name: str,
                        session: Annotated[Session, Depends(get_session)],
                        pairing_token: Annotated[str, Query(min_length=8, max_length=8)] = None):
    user = get_user_by_email(session, email)
    if user is not None:
        raise exceptions.EMAIL_ALREADY_REGISTERED

    # TODO: add checks if token is valid

    user = create_user(session, email, get_password_hash(password), first_name, last_name)

    if chip := get_chip_by_token(session, pairing_token):
        chip.user_id = user.id
        session.commit()
        return {'message': 'User created and Chip successfully paired.'}
    return {'message': 'User successfully created.'}
