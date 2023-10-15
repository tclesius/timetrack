from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.auth.model import TokenResponse
from api.auth.service import authenticate_user, create_access_token
from api.database.session import get_session
from api import exceptions
from api.settings import settings

router = APIRouter(prefix="/auth")


@router.post("/token", response_model=TokenResponse)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 session: Annotated[Session, Depends(get_session)]):
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        return exceptions.LOGIN_EXCEPTION

    access_token_expires = timedelta(minutes=settings.JWT_EXPIRE_MIN)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

