import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class Database:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
                "read_user",
                "password",
                "sistemas-inteligentes.cvqw6muew1ej.us-east-1.rds.amazonaws.com",
                "5432",
                "sistemas_inteligentes",
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
