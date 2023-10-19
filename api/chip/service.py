import secrets
import string

from sqlalchemy.orm import Session

from api.database.schema.chip import Chip


def generate_unique_pairing_token(session: Session, length=8):
    while True:
        token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
        exists = session.query(Chip).filter_by(pairing_token=token).first() is not None
        if not exists:
            return token


def get_chip_by_sn(session: Session, sn: int):
    return session.query(Chip).filter_by(sn=sn).first()


def get_chip_by_token(session: Session, pairing_token: str):
    return session.query(Chip).filter_by(pairing_token=pairing_token).first()
