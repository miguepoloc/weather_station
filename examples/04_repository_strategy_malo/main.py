"""CASO MALO: sin Repository ni Strategy.

Cada endpoint de lectura reimplementa su propio filtro sobre la "base de datos" en memoria y su
propia forma de agregación (total vs. promedio por hora) — duplicado y difícil de testear porque
la lógica de negocio está pegada al almacenamiento.
"""

import fastapi

app = fastapi.FastAPI(title="04 - Repository + Strategy (malo)")

DB: list[dict] = [
    {"node_id": 1, "hour": 8, "temperature": 20.0},
    {"node_id": 1, "hour": 8, "temperature": 22.0},
    {"node_id": 1, "hour": 9, "temperature": 24.0},
]


@app.get("/readings/total")
def get_total(node_id: int):
    # filtro manual...
    result = [r for r in DB if r["node_id"] == node_id]
    return result


@app.get("/readings/hourly-average")
def get_hourly_average(node_id: int):
    # el mismo filtro manual de arriba, vuelto a escribir...
    filtered = [r for r in DB if r["node_id"] == node_id]
    # ...más la lógica de agregación mezclada en el mismo endpoint
    by_hour: dict[int, list[float]] = {}
    for r in filtered:
        by_hour.setdefault(r["hour"], []).append(r["temperature"])
    return [{"hour": h, "avg_temperature": sum(temps) / len(temps)} for h, temps in by_hour.items()]
