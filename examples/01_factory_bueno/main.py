"""CASO BUENO: Factory Method.

Un único lugar (`NodeFactory`) sabe cómo se construye cada tipo de nodo. Los endpoints solo le
piden que cree el nodo — agregar un tercer tipo es agregar un builder, no buscar y editar cada
endpoint que crea nodos.
"""

from abc import ABC, abstractmethod
from typing import Optional

from fastapi import FastAPI, HTTPException

app = FastAPI(title="01 - Factory Method (bueno)")


class NodeBuilder(ABC):
    @abstractmethod
    def build(self, name: str, description: Optional[str], latitude: float, longitude: float) -> dict:
        raise NotImplementedError


class MasterNodeBuilder(NodeBuilder):
    def build(self, name, description, latitude, longitude) -> dict:
        return {"name": name, "description": description, "latitude": latitude, "longitude": longitude, "type": "master", "max_children": 10}


class WorkerNodeBuilder(NodeBuilder):
    def build(self, name, description, latitude, longitude) -> dict:
        return {"name": name, "description": description, "latitude": latitude, "longitude": longitude, "type": "worker", "reports_to": None}


class NodeFactory:
    _builders: dict[str, NodeBuilder] = {"master": MasterNodeBuilder(), "worker": WorkerNodeBuilder()}

    @classmethod
    def create(cls, type_node: str, name: str, description: Optional[str], latitude: float, longitude: float) -> dict:
        builder = cls._builders.get(type_node)
        if builder is None:
            raise HTTPException(400, f"Tipo de nodo inválido: {type_node}")
        return builder.build(name, description, latitude, longitude)


NODES: list[dict] = []
_next_id = 1


def _register(node: dict) -> dict:
    global _next_id
    node["id"] = _next_id
    _next_id += 1
    NODES.append(node)
    return node


@app.post("/nodes")
def create_node(name: str, type_node: str, description: Optional[str] = None, latitude: float = 0, longitude: float = 0):
    return _register(NodeFactory.create(type_node, name, description, latitude, longitude))


@app.post("/nodes/bulk")
def create_nodes_bulk(nodes: list[dict]):
    return [
        _register(NodeFactory.create(n["type_node"], n["name"], n.get("description"), n.get("latitude", 0), n.get("longitude", 0)))
        for n in nodes
    ]


@app.get("/nodes")
def list_nodes():
    return NODES
