"""CASO BUENO: Observer.

`BatterySubject` solo sabe que tiene una lista de observers y los notifica. El endpoint no
conoce ni la cantidad ni el tipo de canales — agregar Slack es un `attach(SlackObserver())`, no
un endpoint reescrito.
"""

from abc import ABC, abstractmethod

from fastapi import FastAPI

app = FastAPI(title="05 - Observer (bueno)")

LOW_BATTERY_THRESHOLD = 10.0


class Observer(ABC):
    @abstractmethod
    def update(self, node_id: int, battery_level: float) -> None:
        raise NotImplementedError


class ConsoleObserver(Observer):
    def update(self, node_id: int, battery_level: float) -> None:
        print(f"[consola] batería baja en nodo {node_id}: {battery_level}V")


class EmailObserver(Observer):
    def update(self, node_id: int, battery_level: float) -> None:
        print(f"[email simulado] Batería baja en nodo {node_id}")


class SmsObserver(Observer):
    def update(self, node_id: int, battery_level: float) -> None:
        print(f"[sms simulado] Batería baja en nodo {node_id}")


class BatterySubject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def check_battery(self, node_id: int, battery_level: float) -> None:
        if battery_level < LOW_BATTERY_THRESHOLD:
            for observer in self._observers:
                observer.update(node_id, battery_level)


battery_subject = BatterySubject()
battery_subject.attach(ConsoleObserver())
battery_subject.attach(EmailObserver())
battery_subject.attach(SmsObserver())
# Agregar Slack mañana: battery_subject.attach(SlackObserver()) — el endpoint de abajo no cambia.


@app.post("/readings")
def save_reading(node_id: int, battery_level: float):
    battery_subject.check_battery(node_id, battery_level)
    return {"node_id": node_id, "battery_level": battery_level}
