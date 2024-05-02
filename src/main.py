from fastapi import FastAPI

from data.router import router as data_router
from nodes.router import router as nodes_router

app = FastAPI()
app.include_router(nodes_router, prefix="/nodes", tags=["nodes"])
app.include_router(data_router, prefix="/data", tags=["data"])


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}
