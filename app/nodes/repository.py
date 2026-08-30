from __future__ import annotations

from sqlalchemy import orm

from app import models


class NodeRepository:
    def __init__(self, db: orm.Session) -> None:
        self._db = db

    def list_all(self) -> list[models.Node]:
        return self._db.query(models.Node).all()

    def create(
        self, name: str, description: str | None, latitude: float, longitude: float, type_: models.NodeType
    ) -> models.Node:
        node = models.Node(name=name, description=description, latitude=latitude, longitude=longitude, type=type_)
        self._db.add(node)
        self._db.commit()
        self._db.refresh(node)
        return node
