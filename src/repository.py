"""This module contains the functions to interact with the database for the auth module."""

from typing import Optional

from src.models import User
from sqlalchemy.orm import Session


def get_user(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()
