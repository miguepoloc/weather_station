from fastapi import FastAPI
from nodes.router import router as nodes_router

app = FastAPI()
app.include_router(nodes_router, prefix="/nodes")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}
