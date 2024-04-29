import os
from typing import Union

from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()

current_dir = os.path.dirname(os.path.realpath(__file__))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/example_dates")
def get_example_dates():
    dates_path = os.path.join(current_dir, 'data', 'example_dates.json')
    return FileResponse(dates_path)


@app.get("/list_nit")
def get_list_nit():
    nit_path = os.path.join(current_dir, 'data', 'list_nit.json')
    return FileResponse(nit_path)
