"""CASO BUENO: Adapter.

`DatabaseGateway` es la única interfaz que le importa a la app: guardar y leer lecturas.
`SQLiteGateway` (por defecto) y `PostgresGateway` la implementan cada uno a su manera. Cambiar de
motor es una variable de entorno (`DB_BACKEND=postgres`), no una búsqueda y reemplazo.
"""

import os
import sqlite3
from abc import ABC, abstractmethod

from fastapi import Depends, FastAPI

app = FastAPI(title="02 - Adapter (bueno)")


class DatabaseGateway(ABC):
    @abstractmethod
    def save_reading(self, node_id: int, temperature: float) -> dict:
        raise NotImplementedError

    @abstractmethod
    def list_readings(self) -> list[dict]:
        raise NotImplementedError


class SQLiteGateway(DatabaseGateway):
    def __init__(self, path: str = "bueno.db") -> None:
        self._path = path
        conn = sqlite3.connect(self._path)
        conn.execute("CREATE TABLE IF NOT EXISTS readings (id INTEGER PRIMARY KEY, node_id INTEGER, temperature REAL)")
        conn.commit()
        conn.close()

    def save_reading(self, node_id: int, temperature: float) -> dict:
        conn = sqlite3.connect(self._path)
        cur = conn.execute("INSERT INTO readings (node_id, temperature) VALUES (?, ?)", (node_id, temperature))
        conn.commit()
        reading_id = cur.lastrowid
        conn.close()
        return {"id": reading_id, "node_id": node_id, "temperature": temperature}

    def list_readings(self) -> list[dict]:
        conn = sqlite3.connect(self._path)
        rows = conn.execute("SELECT id, node_id, temperature FROM readings").fetchall()
        conn.close()
        return [{"id": r[0], "node_id": r[1], "temperature": r[2]} for r in rows]


class PostgresGateway(DatabaseGateway):
    """Requiere `psycopg2-binary` y un Postgres corriendo (ver docker-compose.yml del repo)."""

    def __init__(self, dsn: str) -> None:
        import psycopg2  # import perezoso: solo hace falta si de verdad se usa Postgres

        self._psycopg2 = psycopg2
        self._dsn = dsn
        conn = psycopg2.connect(dsn)
        conn.cursor().execute(
            "CREATE TABLE IF NOT EXISTS readings (id SERIAL PRIMARY KEY, node_id INTEGER, temperature REAL)"
        )
        conn.commit()
        conn.close()

    def save_reading(self, node_id: int, temperature: float) -> dict:
        conn = self._psycopg2.connect(self._dsn)
        cur = conn.cursor()
        cur.execute("INSERT INTO readings (node_id, temperature) VALUES (%s, %s) RETURNING id", (node_id, temperature))
        reading_id = cur.fetchone()[0]
        conn.commit()
        conn.close()
        return {"id": reading_id, "node_id": node_id, "temperature": temperature}

    def list_readings(self) -> list[dict]:
        conn = self._psycopg2.connect(self._dsn)
        rows = conn.cursor().execute("SELECT id, node_id, temperature FROM readings").fetchall()
        conn.close()
        return [{"id": r[0], "node_id": r[1], "temperature": r[2]} for r in rows]


def get_gateway() -> DatabaseGateway:
    if os.getenv("DB_BACKEND") == "postgres":
        return PostgresGateway(os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/estacion_clima"))
    return SQLiteGateway()


gateway = get_gateway()


@app.post("/readings")
def save_reading(node_id: int, temperature: float, db: DatabaseGateway = Depends(lambda: gateway)):
    return db.save_reading(node_id, temperature)


@app.get("/readings")
def get_readings(db: DatabaseGateway = Depends(lambda: gateway)):
    return db.list_readings()
