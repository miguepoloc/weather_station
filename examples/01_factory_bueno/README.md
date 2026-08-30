# 01 · Factory Method — caso bueno

`NodeFactory` es el único lugar que sabe construir cada tipo de nodo. `create_node` y
`create_nodes_bulk` no conocen la diferencia entre un `master` y un `worker` — solo le piden a la
factory que lo resuelva. Agregar un tercer tipo (`NodeType.GATEWAY`) es un nuevo `NodeBuilder`
más una entrada en el diccionario, nada más.

**Corre:**

```bash
uvicorn main:app --reload --port 8002
```

Compara con [`../01_factory_malo`](../01_factory_malo).
