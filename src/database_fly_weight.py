import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

"""
Al patrón de diseño Flyweight. Este patrón se utiliza para minimizar el uso de memoria al compartir tantos datos como
sea posible con objetos similares. En el contexto de las bases de datos, podrías tener una única implementación de la
base de datos y luego tener múltiples “instancias ligeras” que comparten esta implementación pero tienen diferentes
nombres de base de datos.

Database es una clase que implementa el patrón Flyweight. Mantiene un diccionario de instancias de bases de datos que
se han creado, y cuando se solicita una nueva instancia, primero verifica si ya existe una instancia para ese nombre
de base de datos. Si existe, la devuelve; si no existe, crea una nueva instancia, la guarda en el diccionario y
luego la devuelve.

Esto te permite tener múltiples “instancias” de la base de datos que comparten la misma implementación pero tienen
diferentes nombres de base de datos, lo que puede ayudar a reducir el uso de memoria.
"""


class Database:
    instances: dict = {}
    instance = None

    def __new__(cls, "sistemas_inteligentes": str):
        if "sistemas_inteligentes" not in cls.instances:
            instance = super().__new__(cls)
            DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
                "read_user",
                "password",
                "sistemas-inteligentes.cvqw6muew1ej.us-east-1.rds.amazonaws.com",
                "5432",
                "sistemas_inteligentes",
            )
            instance.engine = create_engine(DATABASE_URL)
            instance.session = sessionmaker(autocommit=False, autoflush=False, bind=instance.engine)
            cls.instances["sistemas_inteligentes"] = instance
        return cls.instances["sistemas_inteligentes"]

    def connect(self):
        return self.engine.connect()

    def execute(self, query):
        with self.connect() as connection:
            result = connection.execute(query)
        return result

    def session(self):
        return self.session()


def get_db("sistemas_inteligentes") -> Generator[Session, None, None]:
    db = Database("sistemas_inteligentes")
    db_session = db.session()  # type: ignore
    try:
        yield db_session
    finally:
        db_session.close()
