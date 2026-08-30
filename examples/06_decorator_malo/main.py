"""CASO MALO: sin Decorator.

Cada endpoint mide su propio tiempo de ejecución y revisa a mano su propio diccionario de caché.
El código de negocio (2 líneas) queda enterrado entre 10 líneas de boilerplate repetido.
"""

import time

import fastapi

app = fastapi.FastAPI(title="06 - Decorator (malo)")

_cache: dict = {}


def _expensive_lookup(node_id: int) -> dict:
    time.sleep(0.2)  # simula una consulta costosa
    return {"node_id": node_id, "average_temperature": 21.5}


@app.get("/nodes/{node_id}/summary")
def get_summary(node_id: int):
    # --- boilerplate de timing, copiado en cada endpoint ---
    start = time.perf_counter()
    # --- boilerplate de caché, copiado en cada endpoint ---
    if node_id in _cache:
        print(f"[cache manual] hit para nodo {node_id}")
        result = _cache[node_id]
    else:
        result = _expensive_lookup(node_id)
        _cache[node_id] = result
    elapsed_ms = (time.perf_counter() - start) * 1000
    print(f"[timing manual] get_summary tardó {elapsed_ms:.2f} ms")
    return result
