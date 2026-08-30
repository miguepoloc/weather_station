from __future__ import annotations

import datetime

from sqlalchemy import orm

from app import models


class SensorReadingRepository:
    def __init__(self, db: orm.Session) -> None:
        self._db = db

    def save(
        self, node_id: int, temperature: float, humidity: float, pressure: float, battery_level: float
    ) -> models.SensorReading:
        reading = models.SensorReading(
            node_id=node_id, temperature=temperature, humidity=humidity, pressure=pressure, battery_level=battery_level
        )
        self._db.add(reading)
        self._db.commit()
        self._db.refresh(reading)
        return reading

    def find_by_node(self, node_id: int, start: datetime.datetime, end: datetime.datetime) -> list[models.SensorReading]:
        return (
            self._db.query(models.SensorReading)
            .filter(
                models.SensorReading.node_id == node_id,
                models.SensorReading.date_time >= start,
                models.SensorReading.date_time <= end,
            )
            .all()
        )
