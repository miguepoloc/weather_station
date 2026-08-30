# 06 · Decorator — caso malo

**Problema real:** el timing y el caché están mezclados a mano dentro del endpoint. Cada endpoint
nuevo que quiera medirse o cachearse repite el mismo bloque de 8-10 líneas.

**Corre:**

```bash
uvicorn main:app --reload --port 8011
```

**Pruébalo (la segunda llamada debería ser instantánea):**

```bash
curl http://localhost:8011/nodes/1/summary
curl http://localhost:8011/nodes/1/summary
```

Compara con [`../06_decorator_bueno`](../06_decorator_bueno).
