"""Observer: la lectura de un sensor notifica a quien le interese, sin conocerlos.

CASO MALO (ver examples/05_observer_malo): el endpoint que guarda una lectura llama directo a
`print(...)`, `send_email(...)` y un envío de SMS simulado, uno abajo del otro. Agregar un cuarto
canal de alerta (ej. Slack) implica volver a editar ese endpoint.

CASO BUENO (este archivo): `BatteryAlertSubject` solo sabe que tiene una lista de `Observer`s y
los notifica. `NodeDataFacade` (facade.py) no sabe ni le importa cuántos observers hay ni qué
hacen — agregar un canal nuevo es una línea (`attach(...)`), no un endpoint reescrito.
"""

from __future__ import annotations

import abc
import datetime

from app import constants
from app import models
from app import send_email

LOW_BATTERY_THRESHOLD = 10.0


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, reading: models.SensorReading) -> None:
        raise NotImplementedError


class ConsoleObserver(Observer):
    def update(self, reading: models.SensorReading) -> None:
        print(f"[alerta] batería baja en nodo {reading.node_id}: {reading.battery_level}V")


class EmailObserver(Observer):
    def update(self, reading: models.SensorReading) -> None:
        html = (
            f"<b>Batería baja en el nodo {reading.node_id}</b><br>"
            f"Nivel: {reading.battery_level}V<br>Fecha: {datetime.datetime.utcnow()}"
        )
        send_email.send(to_email=[constants.EnvironmentVariables.ALERT_EMAIL_TO], subject="Batería baja", html=html)


class SmsObserver(Observer):
    def update(self, reading: models.SensorReading) -> None:
        print(f"[sms simulado] Batería baja en nodo {reading.node_id}: {reading.battery_level}V")


class BatteryAlertSubject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify(self, reading: models.SensorReading) -> None:
        for observer in self._observers:
            observer.update(reading)

    def check_battery(self, reading: models.SensorReading) -> None:
        if reading.battery_level < LOW_BATTERY_THRESHOLD:
            self.notify(reading)
