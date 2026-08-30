from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.nodes.factory import NodeFactory
from app.nodes.repository import NodeRepository
from app.schemas import NodeCreate, NodeOut

router = APIRouter()


@router.get("/", response_model=list[NodeOut])
def list_nodes(db: Session = Depends(get_db)) -> list[NodeOut]:
    return NodeRepository(db).list_all()


@router.post("/", response_model=NodeOut)
def create_node(payload: NodeCreate, db: Session = Depends(get_db)) -> NodeOut:
    blueprint = NodeFactory.create_node(
        type_node=payload.type_node,
        name=payload.name,
        description=payload.description,
        latitude=payload.latitude,
        longitude=payload.longitude,
    )
    return NodeRepository(db).create(
        name=blueprint.name,
        description=blueprint.description,
        latitude=blueprint.latitude,
        longitude=blueprint.longitude,
        type_=blueprint.type,
    )
