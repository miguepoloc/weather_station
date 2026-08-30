# 04 · Repository + Strategy — caso malo

**Problema real:** el filtro `[r for r in DB if r["node_id"] == node_id]` está repetido en los dos
endpoints, y la forma de agregar (total vs. promedio por hora) está escrita a mano dentro de cada
uno. Agregar un tercer formato (ej. promedio por día) significa un tercer endpoint con su propio
filtro copiado y su propio bucle de agregación.

**Corre:**

```bash
uvicorn main:app --reload --port 8007
```

Compara con [`../04_repository_strategy_bueno`](../04_repository_strategy_bueno).
