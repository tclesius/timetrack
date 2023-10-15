from sqlalchemy.orm import Session
from api.database.schema.user import User


def get_user_by_token(session: Session, rfid_token: str) -> User | None:
    user = session.query(User).filter(User.rfid_token == rfid_token).first()
    return user


def get_user_by_email(session: Session, email: str) -> User | None:
    user = session.query(User).filter(User.email == email).first()
    return user


def get_user_by_rfid_token(session: Session, rfid_token: str) -> User | None:
    user = session.query(User).filter(User.rfid_token == rfid_token).first()
    return user


def create_user(session: Session,
                rfid_token: str,
                email: str,
                password: str,
                first_name: str,
                last_name: str):
    user = User(rfid_token=rfid_token,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name)

    session.add(user)
    session.commit()
    return user
