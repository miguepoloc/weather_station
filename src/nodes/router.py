from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database_adapter import get_db
from src.models import Nodes
from src.nodes.factory import NodeCreation, NodoFactory
from src.schemas import NodeModel, NodeType
from src.authorizer import get_current_user

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

@router.post("/enviar_email")
async def enviar_email(mensaje: str):
    implementador_email = MensajeroEmail()
    mensajero_normal_email = MensajeroNormal(implementador_email)
    mensajero_normal_email.enviar(mensaje)
    return {"mensaje": "Correo electrónico enviado correctamente"}

@router.post("/enviar_sms")
async def enviar_sms(mensaje: str):
    implementador_sms = MensajeroSMS()
    mensajero_normal_sms = MensajeroNormal(implementador_sms)
    mensajero_normal_sms.enviar(mensaje)
    return {"mensaje": "SMS enviado correctamente"}

@router.post("/enviar_push")
async def enviar_push(mensaje: str):
    implementador_push = MensajeroPush()
    mensajero_normal_push = MensajeroNormal(implementador_push)
    mensajero_normal_push.enviar(mensaje)
    return {"mensaje": "Notificación push enviada correctamente"}