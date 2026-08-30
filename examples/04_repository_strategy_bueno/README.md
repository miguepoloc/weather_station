# 04 · Repository + Strategy — caso bueno

`ReadingRepository` filtra, `AggregationStrategy` agrega, y `get_readings` solo los conecta. Un
solo endpoint sirve para todos los formatos (`?format=total`, `?format=hour`, y el que agregues
después).

**Corre:**

```bash
uvicorn main:app --reload --port 8008
```

**Pruébalo:**

```bash
curl "http://localhost:8008/readings?node_id=1&format=hour"
```

Compara con [`../04_repository_strategy_malo`](../04_repository_strategy_malo).
