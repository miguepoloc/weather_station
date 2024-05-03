from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database_adapter import get_db
from models import Nodes
from nodes.factory import NodeCreation, NodoFactory
from schemas import NodeModel, NodeType
from authorizer import get_current_user

router = APIRouter()


@router.get("/")
def get_nodes(db: Session = Depends(get_db)) -> list[NodeModel]:
    result: list[Nodes] = db.query(Nodes).all()

    return result


@router.post("/create")
def create_node(
    name: str,
    description: Optional[str],
    latitude: float,
    longitude: float,
    type_node: NodeType,
    db: Session = Depends(get_db),
    current_user: dict[str, str] = Depends(get_current_user),
) -> NodeModel:
    node: NodeCreation = NodoFactory.create_node(
        type_node=type_node, name=name, description=description, latitude=latitude, longitude=longitude
    )

    node_model = Nodes(
        name=node.name,
        type=node.type.value,
        description=node.description,
        latitude=node.latitude,
        longitude=node.longitude,
    )

    db.add(node_model)
    db.commit()

    return node_model
