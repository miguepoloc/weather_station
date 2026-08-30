"""CASO MALO: sin Factory Method.

Cada endpoint que necesita crear un nodo repite su propio if/elif por tipo. Si mañana aparece un
tercer tipo de nodo (ej. "gateway"), hay que encontrar y editar CADA COPIA de este bloque.
"""

from typing import Optional

from fastapi import FastAPI, HTTPException

app = FastAPI(title="01 - Factory Method (malo)")

NODES: list[dict] = []
_next_id = 1


@app.post("/nodes")
def create_node(name: str, type_node: str, description: Optional[str] = None, latitude: float = 0, longitude: float = 0):
    global _next_id
    # --- lógica de construcción, copiada y pegada donde haga falta un nodo ---
    if type_node == "master":
        node = {"name": name, "description": description, "latitude": latitude, "longitude": longitude, "type": "master", "max_children": 10}
    elif type_node == "worker":
        node = {"name": name, "description": description, "latitude": latitude, "longitude": longitude, "type": "worker", "reports_to": None}
    else:
        raise HTTPException(400, f"Tipo de nodo inválido: {type_node}")
    # --- fin del bloque duplicado ---
    node["id"] = _next_id
    _next_id += 1
    NODES.append(node)
    return node


@app.post("/nodes/bulk")
def create_nodes_bulk(nodes: list[dict]):
    global _next_id
    created = []
    for n in nodes:
        # el mismo if/elif de arriba, vuelto a escribir aquí porque no hay un lugar común
        if n["type_node"] == "master":
            node = {"name": n["name"], "description": n.get("description"), "latitude": n.get("latitude", 0), "longitude": n.get("longitude", 0), "type": "master", "max_children": 10}
        elif n["type_node"] == "worker":
            node = {"name": n["name"], "description": n.get("description"), "latitude": n.get("latitude", 0), "longitude": n.get("longitude", 0), "type": "worker", "reports_to": None}
        else:
            raise HTTPException(400, f"Tipo de nodo inválido: {n['type_node']}")
        node["id"] = _next_id
        _next_id += 1
        NODES.append(node)
        created.append(node)
    return created


@app.get("/nodes")
def list_nodes():
    return NODES
