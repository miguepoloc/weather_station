from dotenv import load_dotenv
from fastapi import FastAPI

from src.data.router import router as data_router
from src.nodes.router import router as nodes_router
from src.users.router import router as users_router

load_dotenv()

app = FastAPI()
app.include_router(nodes_router, prefix="/nodes", tags=["nodes"])
app.include_router(data_router, prefix="/data", tags=["data"])
app.include_router(users_router, prefix="/users", tags=["users"])


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}
