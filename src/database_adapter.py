import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from abc import ABC, abstractmethod


"""
El patrón Abstract Factory es un patrón de diseño creacional que proporciona una interfaz para crear familias de
objetos relacionados sin especificar sus clases concretas.

En el código proporcionado, AbstractDatabase es una implementación del patrón Abstract Factory. Esta es una clase
abstracta que define la interfaz para todas las bases de datos. DatabasePostgreSQL y DatabaseMySQL son clases concretas
que implementan esta interfaz para PostgreSQL y MySQL, respectivamente.

Esto te permite cambiar de PostgreSQL a MySQL simplemente cambiando DatabasePostgreSQL() por DatabaseMySQL() en la
función get_db(), sin tener que cambiar el resto de tu código.
"""


class AbstractDatabase(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def session(self):
        pass


class DatabasePostgreSQL(AbstractDatabase):
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

    def connect(self):
        return self.engine.connect()

    def session(self):
        return self.session()


class DatabaseMySQL(AbstractDatabase):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            DATABASE_URL = "mysql://{}:{}@{}:{}/{}".format(
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

    def connect(self):
        return self.engine.connect()

    def session(self):
        return self.session()


class DatabaseAdapter:
    def __init__(self, database):
        self.database = database

    def connect(self):
        return self.database.connect()

    def execute(self, query):
        with self.connect() as connection:
            result = connection.execute(query)
        return result

    def session(self):
        return self.database.session()


"""
El patrón Adapter es un patrón de diseño estructural que permite que objetos con interfaces incompatibles colaboren
entre sí. Se utiliza cuando quieres que una clase existente funcione con otras clases sin modificar su código fuente.

En el código proporcionado, DatabaseAdapter es una implementación del patrón Adapter. Esta clase adapta la interfaz de
la clase Database (ya sea DatabasePostgreSQL o DatabaseMySQL) a una interfaz más genérica que tu aplicación puede
utilizar. Esto te permite cambiar la base de datos subyacente sin tener que cambiar el resto de tu código.
"""


def get_db() -> Generator[Session, None, None]:
    # Aquí puedes seleccionar la base de datos que prefieras
    db = DatabaseAdapter(DatabasePostgreSQL())
    db_session = db.session()  # type: ignore
    try:
        yield db_session
    finally:
        db_session.close()
