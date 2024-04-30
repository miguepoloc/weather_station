import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from typing import Generator


class Database:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
                os.getenv("DB_USER"),
                os.getenv("DB_PASS"),
                os.getenv("DB_HOST"),
                os.getenv("DB_PORT"),
                os.getenv("DB_NAME"),
            )
            cls.instance = super().__new__(cls)
            cls.instance.engine = create_engine(DATABASE_URL)
            cls.instance.session = sessionmaker(autocommit=False, autoflush=False, bind=cls.instance.engine)
        return cls.instance


def get_db() -> Generator[Session, None, None]:
    db = Database()
    db_session = db.session()  # type: ignore
    try:
        yield db_session
    finally:
        db_session.close()
