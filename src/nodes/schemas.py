from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class NodeType(Enum):
    MASTER = "master"
    WORKER = "worker"


class NodeModel(BaseModel):
    id: int
    name: str
    type: NodeType
    description: Optional[str] = None
    latitude: float
    longitude: float


class NodesStorageModel(BaseModel):
    id: int
    node_id: int
    date_time: Optional[datetime] = None
    temperature: float
    humidity: float
    pressure: float
    altitude: float
    humidity_hd38: float
    humidity_soil: float
    temperature_soil: float
    conductivity_soil: float
    ph_soil: float
    nitrogen_soil: float
    phosphorus_soil: float
    potassium_soil: float
    battery_level: float
    hour: Optional[int] = None  # This field is only used in the HoursNodesData strategy
    date: Optional[datetime] = None  # This field is only used in the DaysNodesData strategy
