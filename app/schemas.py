from __future__ import annotations

import datetime

import pydantic

from app import models


class NodeCreate(pydantic.BaseModel):
    name: str
    description: str | None = None
    latitude: float
    longitude: float
    type_node: models.NodeType


class NodeOut(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(from_attributes=True)

    id: int
    name: str
    type: models.NodeType
    description: str | None = None
    latitude: float
    longitude: float


class SensorReadingIn(pydantic.BaseModel):
    node_id: int
    temperature: float
    humidity: float
    pressure: float
    battery_level: float


class SensorReadingOut(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(from_attributes=True)

    id: int | None = None
    node_id: int
    date_time: datetime.datetime | None = None
    temperature: float
    humidity: float
    pressure: float
    battery_level: float
