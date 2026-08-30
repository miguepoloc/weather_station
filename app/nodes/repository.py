from __future__ import annotations

from sqlalchemy.orm import Session

from app.models import Node, NodeType


class NodeRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    def list_all(self) -> list[Node]:
        return self._db.query(Node).all()

    def create(self, name: str, description: str | None, latitude: float, longitude: float, type_: NodeType) -> Node:
        node = Node(name=name, description=description, latitude=latitude, longitude=longitude, type=type_)
        self._db.add(node)
        self._db.commit()
        self._db.refresh(node)
        return node
