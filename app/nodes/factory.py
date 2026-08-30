"""Factory Method: centraliza cómo se construye cada tipo de nodo.

CASO MALO (ver examples/01_factory_malo): cada endpoint que necesita crear un nodo repite su
propio `if type_node == "master": ... elif type_node == "worker": ...`. Agregar un tercer tipo de
nodo obliga a encontrar y editar cada copia de ese if/elif.

CASO BUENO (este archivo): un único lugar decide cómo se arma cada tipo de nodo. Los endpoints
solo le piden a `NodeFactory` que cree el nodo — no conocen la diferencia entre un master y un
worker.
"""

from __future__ import annotations

import abc

import pydantic

from app import models


class NodeBlueprint(pydantic.BaseModel):
    name: str
    description: str | None
    latitude: float
    longitude: float
    type: models.NodeType


class NodeBuilder(abc.ABC):
    @abc.abstractmethod
    def build(self, name: str, description: str | None, latitude: float, longitude: float) -> NodeBlueprint:
        raise NotImplementedError


class MasterNodeBuilder(NodeBuilder):
    def build(self, name: str, description: str | None, latitude: float, longitude: float) -> NodeBlueprint:
        return NodeBlueprint(
            name=name, description=description, latitude=latitude, longitude=longitude, type=models.NodeType.MASTER
        )


class WorkerNodeBuilder(NodeBuilder):
    def build(self, name: str, description: str | None, latitude: float, longitude: float) -> NodeBlueprint:
        return NodeBlueprint(
            name=name, description=description, latitude=latitude, longitude=longitude, type=models.NodeType.WORKER
        )


class NodeFactory:
    _builders: dict[models.NodeType, NodeBuilder] = {
        models.NodeType.MASTER: MasterNodeBuilder(),
        models.NodeType.WORKER: WorkerNodeBuilder(),
    }

    @classmethod
    def create_node(
        cls, type_node: models.NodeType, name: str, description: str | None, latitude: float, longitude: float
    ) -> NodeBlueprint:
        builder = cls._builders.get(type_node)
        if builder is None:
            raise ValueError(f"Tipo de nodo inválido: {type_node}")
        return builder.build(name=name, description=description, latitude=latitude, longitude=longitude)
