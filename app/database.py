"""Adapter: una única interfaz de acceso a datos para motores de base de datos distintos.

CASO MALO (el que había antes en este repo, ver git history / examples/02_adapter_malo):
cada módulo que necesitaba una conexión armaba su propia URL de Postgres a mano
(`f"postgresql://{user}:{pass}@{host}/{db}"`) y creaba su propio engine. Cambiar de motor
significaba salir a buscar cada uno de esos lugares y tocarlos uno por uno.

CASO BUENO (este archivo): `DatabaseGateway` define la interfaz que el resto de la app necesita
(una sesión de SQLAlchemy). `SQLiteGateway` y `PostgresGateway` la implementan cada uno a su
manera. El resto del código (routers, repositorios) solo conoce `get_db()` y jamás pregunta qué
motor hay detrás — cambiar de motor es una sola variable de entorno (`DB_BACKEND`), no una
búsqueda y reemplazo por el proyecto.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.constants import EnvironmentVariables


class DatabaseGateway(ABC):
    """La interfaz común que le importa a la aplicación: darle una sesión."""

    @abstractmethod
    def session(self) -> Session:
        raise NotImplementedError


class SQLiteGateway(DatabaseGateway):
    """Motor por defecto: cero configuración, un archivo local `estacion_clima.db`."""

    def __init__(self, database_url: str) -> None:
        self._engine = create_engine(database_url, connect_args={"check_same_thread": False})
        self._session_factory = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

    @property
    def engine(self):
        return self._engine

    def session(self) -> Session:
        return self._session_factory()


class PostgresGateway(DatabaseGateway):
    """Motor de producción. Requiere `psycopg2-binary` y variables DB_* en el entorno."""

    def __init__(self, database_url: str) -> None:
        self._engine = create_engine(database_url)
        self._session_factory = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

    @property
    def engine(self):
        return self._engine

    def session(self) -> Session:
        return self._session_factory()


def _build_gateway() -> DatabaseGateway:
    if EnvironmentVariables.DB_BACKEND == "postgres":
        return PostgresGateway(EnvironmentVariables.DATABASE_URL)
    return SQLiteGateway(EnvironmentVariables.DATABASE_URL)


gateway: DatabaseGateway = _build_gateway()


def get_db() -> Generator[Session, None, None]:
    db = gateway.session()
    try:
        yield db
    finally:
        db.close()
