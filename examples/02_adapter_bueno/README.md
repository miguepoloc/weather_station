# 02 · Adapter — caso bueno

Los endpoints solo conocen `DatabaseGateway` (guardar/leer). No saben si detrás hay SQLite o
Postgres.

**Corre con SQLite (por defecto, cero setup):**

```bash
uvicorn main:app --reload --port 8004
```

**Corre con Postgres (opcional, requiere `docker compose up -d` desde la raíz del repo):**

```bash
DB_BACKEND=postgres DATABASE_URL=postgresql://postgres:postgres@localhost:5432/estacion_clima \
  uvicorn main:app --reload --port 8004
```

Ni un solo endpoint cambió entre los dos modos — esa es la demostración en vivo.

Compara con [`../02_adapter_malo`](../02_adapter_malo).
