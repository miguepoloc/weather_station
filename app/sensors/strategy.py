"""Strategy: la forma de agregar lecturas es intercambiable.

CASO MALO (ver examples/04_repository_strategy_malo): cada endpoint que necesita "totales" o
"promedio por hora" reimplementa su propio bucle de agrupación dentro del handler.

CASO BUENO (este archivo): `AggregationStrategy` define una interfaz común; el endpoint solo
recibe la estrategia correcta según un parámetro y la ejecuta, sin saber cómo agrupa cada una.
"""

from __future__ import annotations

import abc
import itertools

from app import models


class AggregationStrategy(abc.ABC):
    @abc.abstractmethod
    def aggregate(self, readings: list[models.SensorReading]) -> list[dict]:
        raise NotImplementedError


class TotalStrategy(AggregationStrategy):
    """Sin agregación: cada lectura tal cual quedó guardada."""

    def aggregate(self, readings: list[models.SensorReading]) -> list[dict]:
        return [_to_dict(r) for r in readings]


class HourlyAverageStrategy(AggregationStrategy):
    """Una lectura promedio por cada hora del rango."""

    def aggregate(self, readings: list[models.SensorReading]) -> list[dict]:
        ordered = sorted(readings, key=lambda r: r.date_time.hour)
        result: list[dict] = []
        for hour, group in itertools.groupby(ordered, key=lambda r: r.date_time.hour):
            group_list = list(group)
            result.append(
                {
                    "hour": hour,
                    "node_id": group_list[0].node_id,
                    "temperature": _avg(group_list, "temperature"),
                    "humidity": _avg(group_list, "humidity"),
                    "pressure": _avg(group_list, "pressure"),
                    "battery_level": _avg(group_list, "battery_level"),
                }
            )
        return result


def _avg(readings: list[models.SensorReading], field: str) -> float:
    return sum(getattr(r, field) for r in readings) / len(readings)


def _to_dict(reading: models.SensorReading) -> dict:
    return {
        "id": reading.id,
        "node_id": reading.node_id,
        "date_time": reading.date_time,
        "temperature": reading.temperature,
        "humidity": reading.humidity,
        "pressure": reading.pressure,
        "battery_level": reading.battery_level,
    }


def get_strategy(format: str) -> AggregationStrategy:
    strategies: dict[str, AggregationStrategy] = {
        "total": TotalStrategy(),
        "hour": HourlyAverageStrategy(),
    }
    return strategies.get(format, TotalStrategy())
