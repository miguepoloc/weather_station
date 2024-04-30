from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Nodes, NodesStorage
from nodes.schemas import NodeModel, NodesStorageModel
from nodes.service import NodesDataStrategy, get_strategy_format_data

router = APIRouter()


@router.get("/")
def get_nodes(db: Session = Depends(get_db)) -> list[NodeModel]:
    result: list[Nodes] = db.query(Nodes).all()

    return result


@router.get("/data")
def get_nodes_data(
    node_id: int,
    start_date: str,
    end_date: str,
    limit: int = 10,
    db: Session = Depends(get_db),
    format: NodesDataStrategy = Depends(get_strategy_format_data),
) -> list[NodesStorageModel]:
    nodes_storage: list[NodesStorage] = (
        db.query(NodesStorage)
        .filter(
            NodesStorage.node_id == node_id,
            NodesStorage.date_time >= start_date,
            NodesStorage.date_time <= end_date,
        )
        .all()
    )

    result: list = format.get_nodes_data(data=nodes_storage)[:limit]

    return result
