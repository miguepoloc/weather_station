from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import Session

from app.models import SensorReading


class SensorReadingRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    def save(self, node_id: int, temperature: float, humidity: float, pressure: float, battery_level: float) -> SensorReading:
        reading = SensorReading(
            node_id=node_id, temperature=temperature, humidity=humidity, pressure=pressure, battery_level=battery_level
        )
        self._db.add(reading)
        self._db.commit()
        self._db.refresh(reading)
        return reading

    def find_by_node(self, node_id: int, start: datetime, end: datetime) -> list[SensorReading]:
        return (
            self._db.query(SensorReading)
            .filter(SensorReading.node_id == node_id, SensorReading.date_time >= start, SensorReading.date_time <= end)
            .all()
        )
