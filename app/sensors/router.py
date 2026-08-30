from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import SensorReadingIn, SensorReadingOut
from app.sensors.decorators import cache_response, log_execution_time
from app.sensors.facade import NodeDataFacade
from app.sensors.repository import SensorReadingRepository
from app.sensors.strategy import get_strategy

router = APIRouter()


@router.post("/", response_model=SensorReadingOut)
def save_reading(payload: SensorReadingIn, db: Session = Depends(get_db)) -> SensorReadingOut:
    facade = NodeDataFacade(db)
    return facade.record_reading(
        node_id=payload.node_id,
        temperature=payload.temperature,
        humidity=payload.humidity,
        pressure=payload.pressure,
        battery_level=payload.battery_level,
    )


@router.get("/")
@log_execution_time
@cache_response
def get_readings(
    node_id: int,
    start_date: datetime,
    end_date: datetime,
    format: str = "total",
    db: Session = Depends(get_db),
) -> list[dict]:
    readings = SensorReadingRepository(db).find_by_node(node_id=node_id, start=start_date, end=end_date)
    strategy = get_strategy(format)
    return strategy.aggregate(readings)
