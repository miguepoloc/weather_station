from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models import NodeType


class NodeCreate(BaseModel):
    name: str
    description: Optional[str] = None
    latitude: float
    longitude: float
    type_node: NodeType


class NodeOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    type: NodeType
    description: Optional[str] = None
    latitude: float
    longitude: float


class SensorReadingIn(BaseModel):
    node_id: int
    temperature: float
    humidity: float
    pressure: float
    battery_level: float


class SensorReadingOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    node_id: int
    date_time: Optional[datetime] = None
    temperature: float
    humidity: float
    pressure: float
    battery_level: float
