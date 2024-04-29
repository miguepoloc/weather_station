from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Nodes
from nodes.schemas import NodeModel

router = APIRouter()


@router.get("/")
def get_nodes(db: Session = Depends(get_db)) -> list[NodeModel]:
    result: list[Nodes] = db.query(Nodes).all()

    return result
