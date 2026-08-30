"""CASO MALO: sin Facade.

El endpoint que guarda una lectura hace TODO inline: valida, guarda, revisa la batería y manda
las 3 notificaciones. Si un script de importación masiva necesita el mismo flujo, copia y pega
este bloque completo.
"""

import fastapi

app = fastapi.FastAPI(title="03 - Facade (malo)")

READINGS: list[dict] = []
_next_id = 1

LOW_BATTERY_THRESHOLD = 10.0


@app.post("/readings")
def save_reading(node_id: int, temperature: float, battery_level: float):
    global _next_id
    # 1) guardar
    reading = {"id": _next_id, "node_id": node_id, "temperature": temperature, "battery_level": battery_level}
    _next_id += 1
    READINGS.append(reading)

    # 2) revisar batería y notificar — mezclado en el mismo endpoint
    if battery_level < LOW_BATTERY_THRESHOLD:
        print(f"[alerta consola] batería baja en nodo {node_id}: {battery_level}V")
        print(f"[email simulado] to=docente@example.com asunto='Batería baja en nodo {node_id}'")
        print(f"[sms simulado] Batería baja en nodo {node_id}: {battery_level}V")

    return reading


@app.get("/readings")
def list_readings():
    return READINGS
