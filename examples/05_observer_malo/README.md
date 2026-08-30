# 05 · Observer — caso malo

**Problema real:** `save_reading` conoce los 3 canales de notificación por su nombre y los llama
uno por uno. Agregar o quitar un canal significa editar este endpoint (y cualquier otro que
también dispare alertas de batería).

**Corre:**

```bash
uvicorn main:app --reload --port 8009
```

Compara con [`../05_observer_bueno`](../05_observer_bueno).
