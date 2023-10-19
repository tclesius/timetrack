from sqlalchemy.orm import Session
from api.database.schema.user import User


def get_user_by_email(session: Session, email: str) -> User | None:
    user = session.query(User).filter(User.email == email).first()
    return user


def create_user(session: Session,
                chip_token: str,
                email: str,
                password: str,
                first_name: str,
                last_name: str):
    user = User(chip_token=chip_token,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name)

    session.add(user)
    session.commit()
    return user
