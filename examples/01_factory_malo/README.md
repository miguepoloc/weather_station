# 01 · Factory Method — caso malo

**Problema real:** `create_node` y `create_nodes_bulk` repiten el mismo `if/elif` por tipo de
nodo. Agregar un tercer tipo, o cambiar cómo se arma un `worker`, obliga a tocar los dos lugares
(y cualquier otro que aparezca después).

**Corre:**

```bash
uvicorn main:app --reload --port 8001
```

**Pruébalo:**

```bash
curl -X POST "http://localhost:8001/nodes?name=NodoA&type_node=master&latitude=10&longitude=-74"
```

Compara con [`../01_factory_bueno`](../01_factory_bueno).
