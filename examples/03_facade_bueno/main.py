"""CASO BUENO: Facade.

`WeatherFacade.record_reading` es el único lugar que conoce el flujo completo (guardar + revisar
batería + notificar). El endpoint queda en una línea, y cualquier otro caller (otro endpoint, un
script, un test) reutiliza exactamente el mismo comportamiento sin copiar nada.
"""

from fastapi import FastAPI

app = FastAPI(title="03 - Facade (bueno)")

LOW_BATTERY_THRESHOLD = 10.0


class ReadingRepository:
    def __init__(self) -> None:
        self._readings: list[dict] = []
        self._next_id = 1

    def save(self, node_id: int, temperature: float, battery_level: float) -> dict:
        reading = {"id": self._next_id, "node_id": node_id, "temperature": temperature, "battery_level": battery_level}
        self._next_id += 1
        self._readings.append(reading)
        return reading

    def list_all(self) -> list[dict]:
        return self._readings


class BatteryNotifier:
    def notify_if_low(self, reading: dict) -> None:
        if reading["battery_level"] >= LOW_BATTERY_THRESHOLD:
            return
        node_id, level = reading["node_id"], reading["battery_level"]
        print(f"[alerta consola] batería baja en nodo {node_id}: {level}V")
        print(f"[email simulado] to=docente@example.com asunto='Batería baja en nodo {node_id}'")
        print(f"[sms simulado] Batería baja en nodo {node_id}: {level}V")


class WeatherFacade:
    def __init__(self) -> None:
        self._repository = ReadingRepository()
        self._notifier = BatteryNotifier()

    def record_reading(self, node_id: int, temperature: float, battery_level: float) -> dict:
        reading = self._repository.save(node_id, temperature, battery_level)
        self._notifier.notify_if_low(reading)
        return reading

    def list_readings(self) -> list[dict]:
        return self._repository.list_all()


facade = WeatherFacade()


@app.post("/readings")
def save_reading(node_id: int, temperature: float, battery_level: float):
    return facade.record_reading(node_id, temperature, battery_level)


@app.get("/readings")
def list_readings():
    return facade.list_readings()
