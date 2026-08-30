# 05 · Observer — caso bueno

`BatterySubject` no sabe qué hacen sus observers, solo que existen. El endpoint no conoce ningún
canal de notificación en absoluto.

**Corre:**

```bash
uvicorn main:app --reload --port 8010
```

Compara con [`../05_observer_malo`](../05_observer_malo).
