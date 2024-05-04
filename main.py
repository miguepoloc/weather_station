from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from src.data.router import router as data_router
from src.nodes.router import router as nodes_router
from src.users.router import router as users_router
from cadena_de_responsabilidad import ManejadorDescuento,ManejadorPremium,ManejadorVIP
load_dotenv()

app = FastAPI()
app.include_router(nodes_router, prefix="/nodes", tags=["nodes"])
app.include_router(data_router, prefix="/data", tags=["data"])
app.include_router(users_router, prefix="/users", tags=["users"])


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}

class SolicitudDescuento(BaseModel):
    tipo_cliente: str
    monto: float

@app.post("/descuento_js/")
async def calcular_descuento(solicitud: SolicitudDescuento):
    manejador_vip = ManejadorVIP()
    manejador_premium = ManejadorPremium(manejador_vip)
    manejador_descuento = ManejadorDescuento(manejador_premium)

    descuento = manejador_descuento.manejar_solicitud(solicitud.dict())
    return {"descuento_aplicado": descuento}

#ejempo de clientes
    """
    solicitudes = [
        {'tipo_cliente': 'nuevo_cliente', 'monto': 100},
        {'tipo_cliente': 'premium', 'monto': 200},
        {'tipo_cliente': 'vip', 'monto': 300},
        {'tipo_cliente': 'regular', 'monto': 400}
    ]
"""