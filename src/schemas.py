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
    id: Optional[int] = None
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


class UserModel(BaseModel):
    id: int
    email: str
    password: str
    first_name: str
    last_name: str
    document: Optional[str] = None
    code_phone: Optional[str] = None
    phone_number: Optional[str] = None
    is_admin: bool = False
    is_superuser: bool = False
    profile_image: Optional[str] = None
    city: Optional[str] = None

    class Config:
        orm_mode = True
