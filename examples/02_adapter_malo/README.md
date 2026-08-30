# 02 · Adapter — caso malo

**Problema real:** `sqlite3.connect(DB_PATH)` está repetido en cada endpoint. Cambiar de motor de
base de datos (a Postgres, por ejemplo) significa encontrar cada una de esas líneas y
reescribirlas — y todo lo que use `conn.execute(...)` con sintaxis específica de SQLite.

**Corre:**

```bash
uvicorn main:app --reload --port 8003
```

Compara con [`../02_adapter_bueno`](../02_adapter_bueno).
