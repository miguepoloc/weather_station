"""Decorator: comportamiento transversal (logging, caché) sin tocar el cuerpo del endpoint.

CASO MALO (ver examples/06_decorator_malo): cada endpoint mide su propio tiempo de ejecución con
un `start = time.time()` / `print(...)` al final, y revisa a mano un diccionario de caché antes de
calcular la respuesta — copiado y pegado en cada función.

CASO BUENO (este archivo): `@log_execution_time` y `@cache_response` son genéricos y se aplican
declarativamente. El endpoint solo tiene su lógica de negocio.
"""

from __future__ import annotations

import functools
import time
from collections.abc import Callable

_cache: dict[tuple, object] = {}

# Los parámetros inyectados por FastAPI (como `db`, una sesión distinta en cada request) no deben
# formar parte de la clave: si se incluyeran, el caché jamás daría un "hit" porque ese valor
# cambia siempre, aunque el resto de argumentos sea idéntico.
_CACHE_IGNORE_KWARGS = {"db"}


def log_execution_time(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"[timing] {func.__name__} tardó {elapsed_ms:.2f} ms")
        return result

    return wrapper


def cache_response(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        relevant_kwargs = {k: v for k, v in kwargs.items() if k not in _CACHE_IGNORE_KWARGS}
        key = (func.__name__, args, tuple(sorted(relevant_kwargs.items())))
        if key in _cache:
            print(f"[cache] hit para {func.__name__}")
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        return result

    return wrapper
