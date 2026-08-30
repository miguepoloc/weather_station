import fastapi
from sqlalchemy import orm

from app import database
from app import schemas
from app.nodes import factory
from app.nodes import repository

router = fastapi.APIRouter()


@router.get("/", response_model=list[schemas.NodeOut])
def list_nodes(db: orm.Session = fastapi.Depends(database.get_db)) -> list[schemas.NodeOut]:
    return repository.NodeRepository(db).list_all()


@router.post("/", response_model=schemas.NodeOut)
def create_node(payload: schemas.NodeCreate, db: orm.Session = fastapi.Depends(database.get_db)) -> schemas.NodeOut:
    blueprint = factory.NodeFactory.create_node(
        type_node=payload.type_node,
        name=payload.name,
        description=payload.description,
        latitude=payload.latitude,
        longitude=payload.longitude,
    )
    return repository.NodeRepository(db).create(
        name=blueprint.name,
        description=blueprint.description,
        latitude=blueprint.latitude,
        longitude=blueprint.longitude,
        type_=blueprint.type,
    )
