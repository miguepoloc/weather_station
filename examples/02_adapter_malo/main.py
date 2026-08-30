"""CASO MALO: sin Adapter.

Cada endpoint abre su propia conexión SQLite hardcodeada. Si mañana el proyecto crece y hay que
usar Postgres en producción, hay que ir función por función cambiando `sqlite3.connect(...)` por
el cliente de Postgres — y rezar por no dejar ninguna sin tocar.
"""

import sqlite3

from fastapi import FastAPI

app = FastAPI(title="02 - Adapter (malo)")

DB_PATH = "malo.db"


def _init_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS readings (id INTEGER PRIMARY KEY, node_id INTEGER, temperature REAL)")
    conn.commit()
    conn.close()


_init_db()


@app.post("/readings")
def save_reading(node_id: int, temperature: float):
    # Conexión SQLite hardcodeada — se repite igual en get_readings de abajo
    conn = sqlite3.connect(DB_PATH)
    cur = conn.execute("INSERT INTO readings (node_id, temperature) VALUES (?, ?)", (node_id, temperature))
    conn.commit()
    reading_id = cur.lastrowid
    conn.close()
    return {"id": reading_id, "node_id": node_id, "temperature": temperature}


@app.get("/readings")
def get_readings():
    # Misma conexión SQLite hardcodeada, otra vez
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT id, node_id, temperature FROM readings").fetchall()
    conn.close()
    return [{"id": r[0], "node_id": r[1], "temperature": r[2]} for r in rows]
