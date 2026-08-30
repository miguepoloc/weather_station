# 03 · Facade — caso malo

**Problema real:** `save_reading` mezcla persistencia (guardar la lectura) con orquestación
(revisar batería + 3 canales de notificación). Es real: viene casi literal del endpoint
`POST /data/save_data` que tenía este repo antes de esta clase. Si otro flujo (un import masivo,
un test) necesita "guardar y notificar", copia y pega el bloque completo.

**Corre:**

```bash
uvicorn main:app --reload --port 8005
```

Compara con [`../03_facade_bueno`](../03_facade_bueno).
