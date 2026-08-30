"""CASO BUENO: Decorator.

`@log_execution_time` y `@cache_response` son genéricos y reutilizables. El endpoint solo tiene
su lógica de negocio — el timing y el caché se agregan declarativamente, sin tocar el cuerpo de
la función.
"""

import time
from functools import wraps

from fastapi import FastAPI

app = FastAPI(title="06 - Decorator (bueno)")

_cache: dict = {}


def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"[timing] {func.__name__} tardó {elapsed_ms:.2f} ms")
        return result

    return wrapper


def cache_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key in _cache:
            print(f"[cache] hit para {func.__name__}")
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        return result

    return wrapper


def _expensive_lookup(node_id: int) -> dict:
    time.sleep(0.2)  # simula una consulta costosa
    return {"node_id": node_id, "average_temperature": 21.5}


@app.get("/nodes/{node_id}/summary")
@log_execution_time
@cache_response
def get_summary(node_id: int):
    return _expensive_lookup(node_id)
