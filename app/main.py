from dotenv import load_dotenv
from fastapi import FastAPI

from app.database import gateway
from app.models import Base
from app.nodes.router import router as nodes_router
from app.sensors.router import router as sensors_router
from app.users.router import router as users_router

load_dotenv()

Base.metadata.create_all(bind=gateway.engine)

app = FastAPI(
    title="Estación Climática",
    description="API de ejemplo: 6 patrones de diseño GoF aplicados a una estación IoT real.",
)
app.include_router(nodes_router, prefix="/nodes", tags=["nodes"])
app.include_router(sensors_router, prefix="/sensors", tags=["sensors"])
app.include_router(users_router, prefix="/users", tags=["users"])


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Estación Climática funcionando"}
