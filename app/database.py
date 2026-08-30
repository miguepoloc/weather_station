"""Adapter + Factory Method + Singleton: acceso a datos intercambiable, construido una sola vez.

CASO MALO (el que había antes en este repo, ver git history / examples/02_adapter_malo):
cada módulo que necesitaba una conexión armaba su propia URL de Postgres a mano
(`f"postgresql://{user}:{pass}@{host}/{db}"`) y creaba su propio engine. Cambiar de motor
significaba salir a buscar cada uno de esos lugares y tocarlos uno por uno.

CASO BUENO (este archivo), tres patrones trabajando juntos:

- **Adapter**: `DatabaseGateway` define la interfaz que el resto de la app necesita (una sesión
  de SQLAlchemy). `SQLiteGateway` y `PostgresGateway` la implementan cada uno a su manera. El
  resto del código (routers, repositorios) solo conoce `get_db()` y jamás pregunta qué motor hay
  detrás.
- **Factory Method**: `DatabaseGatewayFactory.create()` es el único lugar que decide cuál
  implementación instanciar. Cambiar de motor es una variable de entorno (`DB_BACKEND`), no una
  búsqueda y reemplazo por el proyecto.
- **Singleton**: `SingletonMeta` garantiza que cada gateway concreto (`SQLiteGateway`,
  `PostgresGateway`) se construya una sola vez — el engine y el pool de conexiones de SQLAlchemy
  no se recrean en cada import ni en cada request.
"""

from __future__ import annotations

import abc
import threading
from collections.abc import Generator

import sqlalchemy
from sqlalchemy import orm

from app import constants


class SingletonMeta(abc.ABCMeta):
    """Metaclase genérica: como máximo una instancia por clase concreta.

    Hereda de `abc.ABCMeta` (en vez de `type`) para poder aplicarse a clases que también son
    `abc.ABC` sin choque de metaclases.
    """

    _instances: dict[type, object] = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseGateway(abc.ABC, metaclass=SingletonMeta):
    """La interfaz común que le importa a la aplicación: darle una sesión."""

    @abc.abstractmethod
    def session(self) -> orm.Session: ...


class SQLiteGateway(DatabaseGateway):
    """Motor por defecto: cero configuración, un archivo local `estacion_clima.db`."""

    def __init__(self, database_url: str) -> None:
        self._engine = sqlalchemy.create_engine(database_url, connect_args={"check_same_thread": False})
        self._session_factory = orm.sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

    @property
    def engine(self) -> sqlalchemy.Engine:
        return self._engine

    def session(self) -> orm.Session:
        return self._session_factory()


class PostgresGateway(DatabaseGateway):
    """Motor de producción. Requiere `psycopg2-binary` y variables DB_* en el entorno."""

    def __init__(self, database_url: str) -> None:
        self._engine = sqlalchemy.create_engine(database_url)
        self._session_factory = orm.sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

    @property
    def engine(self) -> sqlalchemy.Engine:
        return self._engine

    def session(self) -> orm.Session:
        return self._session_factory()


class DatabaseGatewayFactory:
    """Factory Method: el único lugar que decide qué motor concreto se instancia."""

    @staticmethod
    def create() -> DatabaseGateway:
        if constants.EnvironmentVariables.DB_BACKEND == "postgres":
            return PostgresGateway(constants.EnvironmentVariables.DATABASE_URL)
        return SQLiteGateway(constants.EnvironmentVariables.DATABASE_URL)


gateway: DatabaseGateway = DatabaseGatewayFactory.create()


def get_db() -> Generator[orm.Session, None, None]:
    db = gateway.session()
    try:
        yield db
    finally:
        db.close()
