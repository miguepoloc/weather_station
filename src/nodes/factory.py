from abc import ABC, abstractmethod
from typing import Optional

from src.schemas import NodeType


class NodeCreation(ABC):
    @abstractmethod
    def __init__(self, name: str, description: Optional[str], latitude: float, longitude: float) -> None:
        self.name: str = name
        self.description: str | None = description
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.type: NodeType


class NodeFather(NodeCreation):
    def __init__(self, name: str, description: Optional[str], latitude: float, longitude: float):
        super().__init__(name=name, description=description, latitude=latitude, longitude=longitude)
        self.type = NodeType.MASTER

class NodeChild(NodeCreation):
    def __init__(self, name: str, description: Optional[str], latitude: float, longitude: float):
        super().__init__(name=name, description=description, latitude=latitude, longitude=longitude)
        self.type = NodeType.WORKER


class NodoFactory:
    @staticmethod
    def create_node(
        type_node: NodeType, name: str, description: Optional[str], latitude: float, longitude: float
    ) -> NodeCreation:
        if type_node == NodeType.MASTER:
            return NodeFather(name=name, description=description, latitude=latitude, longitude=longitude)
        elif type_node == NodeType.WORKER:
            return NodeChild(name=name, description=description, latitude=latitude, longitude=longitude)
        else:
            raise ValueError(f"Invalid type {type_node} to create node")
