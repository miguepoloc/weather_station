"""Facade: una sola llamada esconde "guardar + revisar batería + notificar".

CASO MALO (ver examples/03_facade_malo): el endpoint que recibe una lectura hace, todo inline:
construye el objeto, hace commit, arma el subject, adjunta los observers y revisa la batería.
Si mañana otro endpoint (ej. un import masivo) necesita hacer lo mismo, copia y pega ese bloque.

CASO BUENO (este archivo): `NodeDataFacade.record_reading` es el único lugar que conoce ese flujo
completo. Cualquier endpoint (o script, o test) que necesite "registrar una lectura" solo llama a
esto.
"""

from __future__ import annotations

from sqlalchemy import orm

from app import models
from app.sensors import observer
from app.sensors import repository


class NodeDataFacade:
    def __init__(self, db: orm.Session) -> None:
        self._repository = repository.SensorReadingRepository(db)
        self._battery_alerts = observer.BatteryAlertSubject()
        self._battery_alerts.attach(observer.ConsoleObserver())
        self._battery_alerts.attach(observer.EmailObserver())
        self._battery_alerts.attach(observer.SmsObserver())

    def record_reading(
        self, node_id: int, temperature: float, humidity: float, pressure: float, battery_level: float
    ) -> models.SensorReading:
        reading = self._repository.save(
            node_id=node_id, temperature=temperature, humidity=humidity, pressure=pressure, battery_level=battery_level
        )
        self._battery_alerts.check_battery(reading)
        return reading
