# 06 · Decorator — caso bueno

`get_summary` es una línea de lógica de negocio. El timing y el caché se aplican declarando dos
decoradores encima — reutilizables en cualquier otro endpoint del proyecto sin copiar nada.

**Corre:**

```bash
uvicorn main:app --reload --port 8012
```

**Pruébalo (la segunda llamada debería ser instantánea y loguear `[cache] hit`):**

```bash
curl http://localhost:8012/nodes/1/summary
curl http://localhost:8012/nodes/1/summary
```

Compara con [`../06_decorator_malo`](../06_decorator_malo).
