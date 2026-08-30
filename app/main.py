import dotenv
import fastapi

from app import database
from app import models
from app.nodes import router as nodes_router
from app.sensors import router as sensors_router
from app.users import router as users_router

dotenv.load_dotenv()

models.Base.metadata.create_all(bind=database.gateway.engine)

app = fastapi.FastAPI(
    title="Estación Climática",
    description="API de ejemplo: 6 patrones de diseño GoF aplicados a una estación IoT real.",
)
app.include_router(nodes_router.router, prefix="/nodes", tags=["nodes"])
app.include_router(sensors_router.router, prefix="/sensors", tags=["sensors"])
app.include_router(users_router.router, prefix="/users", tags=["users"])


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Estación Climática funcionando"}
