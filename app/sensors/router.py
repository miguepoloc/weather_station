import datetime

import fastapi
from sqlalchemy import orm

from app import database
from app import schemas
from app.sensors import decorators
from app.sensors import facade
from app.sensors import repository
from app.sensors import strategy

router = fastapi.APIRouter()


@router.post("/", response_model=schemas.SensorReadingOut)
def save_reading(payload: schemas.SensorReadingIn, db: orm.Session = fastapi.Depends(database.get_db)) -> schemas.SensorReadingOut:
    node_facade = facade.NodeDataFacade(db)
    return node_facade.record_reading(
        node_id=payload.node_id,
        temperature=payload.temperature,
        humidity=payload.humidity,
        pressure=payload.pressure,
        battery_level=payload.battery_level,
    )


@router.get("/")
@decorators.log_execution_time
@decorators.cache_response
def get_readings(
    node_id: int,
    start_date: datetime.datetime,
    end_date: datetime.datetime,
    format: str = "total",
    db: orm.Session = fastapi.Depends(database.get_db),
) -> list[dict]:
    readings = repository.SensorReadingRepository(db).find_by_node(node_id=node_id, start=start_date, end=end_date)
    aggregation_strategy = strategy.get_strategy(format)
    return aggregation_strategy.aggregate(readings)
