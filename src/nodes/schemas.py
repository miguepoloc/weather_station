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
