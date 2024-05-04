from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.data.observer import ConsoleObserver, EmailObserver, NodeSubject, SmsObserver
from src.data.strategy import NodesDataStrategy
from src.data.utils import get_strategy_format_data
from src.database import get_db
from src.models import NodesStorage
from src.schemas import NodesStorageModel

router = APIRouter()


@router.get("/")
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


@router.post("/save_data")
def save_data(node_data: NodesStorageModel, db: Session = Depends(get_db)) -> NodesStorageModel:
    node_storage: NodesStorage = NodesStorage(
        node_id=node_data.node_id,
        date_time=node_data.date_time,
        temperature=node_data.temperature,
        humidity=node_data.humidity,
        pressure=node_data.pressure,
        altitude=node_data.altitude,
        humidity_hd38=node_data.humidity_hd38,
        humidity_soil=node_data.humidity_soil,
        temperature_soil=node_data.temperature_soil,
        conductivity_soil=node_data.conductivity_soil,
        ph_soil=node_data.ph_soil,
        nitrogen_soil=node_data.nitrogen_soil,
        phosphorus_soil=node_data.phosphorus_soil,
        potassium_soil=node_data.potassium_soil,
        battery_level=node_data.battery_level,
    )

    db.add(node_storage)
    db.commit()

    node_subject = NodeSubject(node=node_data)
    node_subject.attach(ConsoleObserver())
    node_subject.attach(EmailObserver())
    node_subject.attach(SmsObserver())

    node_subject.check_battery()
    return node_data

