from datetime import timedelta, datetime, UTC
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from api.database.session import get_session
from api import exceptions
from api.settings import settings
from api.user.service import get_user_by_email

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(hashed_password, plain_password):
    print(plain_password, hashed_password)
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(session: Annotated[Session, Depends(get_session)], email: str, password: str):
    user = get_user_by_email(session, email)
    if user is None or not verify_password(user.password, password):
        raise exceptions.LOGIN_EXCEPTION
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


def get_current_user(session: Annotated[Session, Depends(get_session)],
                     token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="/auth/token"))]):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise exceptions.CREDENTIALS_EXCEPTION
    except JWTError:
        raise exceptions.CREDENTIALS_EXCEPTION
    user = get_user_by_email(session, email)
    if user is None:
        raise exceptions.CREDENTIALS_EXCEPTION
    return user
