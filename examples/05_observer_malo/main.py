"""CASO MALO: sin Observer.

El endpoint llama directo a cada canal de notificación. Agregar un canal nuevo (ej. Slack) o
quitar uno (ej. dejar de mandar SMS) significa editar este endpoint.
"""

import fastapi

app = fastapi.FastAPI(title="05 - Observer (malo)")

LOW_BATTERY_THRESHOLD = 10.0


@app.post("/readings")
def save_reading(node_id: int, battery_level: float):
    if battery_level < LOW_BATTERY_THRESHOLD:
        print(f"[consola] batería baja en nodo {node_id}: {battery_level}V")
        print(f"[email simulado] Batería baja en nodo {node_id}")
        print(f"[sms simulado] Batería baja en nodo {node_id}")
        # si mañana piden Slack, se agrega OTRA línea aquí, y otra vez, y otra vez...

    return {"node_id": node_id, "battery_level": battery_level}
