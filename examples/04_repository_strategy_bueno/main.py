"""CASO BUENO: Repository + Strategy.

`ReadingRepository` es el único lugar que sabe filtrar los datos. `AggregationStrategy` es el
único lugar que sabe agregar. El endpoint solo pide los datos y elige la estrategia por un
parámetro — agregar un tercer formato es una clase nueva, no un endpoint nuevo.
"""

from abc import ABC, abstractmethod

from fastapi import Depends, FastAPI

app = FastAPI(title="04 - Repository + Strategy (bueno)")

DB: list[dict] = [
    {"node_id": 1, "hour": 8, "temperature": 20.0},
    {"node_id": 1, "hour": 8, "temperature": 22.0},
    {"node_id": 1, "hour": 9, "temperature": 24.0},
]


class ReadingRepository:
    def find_by_node(self, node_id: int) -> list[dict]:
        return [r for r in DB if r["node_id"] == node_id]


class AggregationStrategy(ABC):
    @abstractmethod
    def aggregate(self, readings: list[dict]) -> list[dict]:
        raise NotImplementedError


class TotalStrategy(AggregationStrategy):
    def aggregate(self, readings: list[dict]) -> list[dict]:
        return readings


class HourlyAverageStrategy(AggregationStrategy):
    def aggregate(self, readings: list[dict]) -> list[dict]:
        by_hour: dict[int, list[float]] = {}
        for r in readings:
            by_hour.setdefault(r["hour"], []).append(r["temperature"])
        return [{"hour": h, "avg_temperature": sum(temps) / len(temps)} for h, temps in by_hour.items()]


def get_strategy(format: str = "total") -> AggregationStrategy:
    return {"total": TotalStrategy(), "hour": HourlyAverageStrategy()}.get(format, TotalStrategy())


repository = ReadingRepository()


@app.get("/readings")
def get_readings(node_id: int, strategy: AggregationStrategy = Depends(get_strategy)):
    return strategy.aggregate(repository.find_by_node(node_id))
