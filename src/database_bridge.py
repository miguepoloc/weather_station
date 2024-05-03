import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from abc import ABC, abstractmethod


"""
El patrón de diseño Bridge se utiliza para separar una abstracción de su implementación, de modo que las dos puedan
variar independientemente. Esto es especialmente útil cuando necesitas cambiar la implementación en tiempo de ejecución.

En el contexto de tu aplicación, podrías tener una abstracción Database que define las operaciones que tu aplicación
necesita (como connect, execute y session), y luego tener diferentes implementaciones de esta abstracción para
diferentes bases de datos.

Database es una clase abstracta que define la interfaz para todas las bases de datos. PostgreSQL y MySQL son clases
concretas que implementan esta interfaz para PostgreSQL y MySQL, respectivamente.

Para cambiar de PostgreSQL a MySQL, solo necesitarías cambiar el valor de la variable db_type en la función get_db()
de PostgreSQL a MySQL, sin tener que cambiar el resto de tu código.

"""


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def session(self):
        pass


class PostgreSQL(Database):
    def __init__(self):
        DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
            os.getenv("DB_USER"),
            os.getenv("DB_PASS"),
            os.getenv("DB_HOST"),
            os.getenv("DB_PORT"),
            os.getenv("DB_NAME"),
        )
        self.engine = create_engine(DATABASE_URL)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def connect(self):
        return self.engine.connect()

    def session(self):
        return self.session()


class MySQL(Database):
    def __init__(self):
        DATABASE_URL = "mysql://{}:{}@{}:{}/{}".format(
            os.getenv("DB_USER"),
            os.getenv("DB_PASS"),
            os.getenv("DB_HOST"),
            os.getenv("DB_PORT"),
            os.getenv("DB_NAME"),
        )
        self.engine = create_engine(DATABASE_URL)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def connect(self):
        return self.engine.connect()

    def session(self):
        return self.session()


def get_db(db_type) -> Generator[Session, None, None]:
    # Aquí puedes seleccionar la base de datos que prefieras
    db: PostgreSQL | MySQL = PostgreSQL() if db_type == "postgresql" else MySQL()
    db_session = db.session()  # type: ignore
    try:
        yield db_session
    finally:
        db_session.close()
