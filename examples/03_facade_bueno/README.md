# 03 · Facade — caso bueno

`WeatherFacade.record_reading` esconde la orquestación (guardar + revisar batería + notificar)
detrás de una sola llamada. El endpoint no sabe cómo se guarda ni cómo se notifica — solo le pide
al facade que registre la lectura.

**Corre:**

```bash
uvicorn main:app --reload --port 8006
```

Compara con [`../03_facade_malo`](../03_facade_malo).
