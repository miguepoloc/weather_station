from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()

class Restaurante:
    def __init__(self):
        self.menu = {}
        self.pedidos = []

    def agregar_plato_al_menu(self, nombre, precio):
        self.menu[nombre] = precio

    def realizar_orden(self, pedido):
        self.pedidos.append(pedido)

    def mostrar_ordenes(self):
        return self.pedidos

    def mostrar_menu(self):
        return self.menu

class Pedido:
    def __init__(self):
        self.platos = []

    def agregar_plato(self, nombre):
        self.platos.append(nombre)

    def __str__(self):
        return ", ".join(self.platos)

class PedidoBuilder:
    def __init__(self):
        self.pedido = Pedido()

    def agregar_plato(self, nombre):
        self.pedido.agregar_plato(nombre)

    def obtener_pedido(self):
        return self.pedido

restaurante = Restaurante()

@router.post("/crear_plato/")
async def crear_plato(nombre: str, precio: float):
    restaurante.agregar_plato_al_menu(nombre, precio)
    return {"message": "Plato creado exitosamente"}

class PedidoRequest(BaseModel):
    platos: List[str]

@router.post("/realizar_pedido/")
async def confirmar_pedido(request: PedidoRequest):
    try:
        platos = request.platos
        for plato in platos:
            if plato not in restaurante.menu:
                return {"message": f"Error: El plato '{plato}' no existe en el menú."}

        pedido_builder = PedidoBuilder()
        for plato in platos:
            pedido_builder.agregar_plato(plato)

        pedido = pedido_builder.obtener_pedido()

        restaurante.realizar_orden(pedido)
        print("PEDIDO:", pedido)
        return {"message": "Pedido realizado exitosamente"}
    except Exception as e:
        print("Error al realizar pedido:", e)
        return {"message": "Error al realizar pedido"}

@router.get("/ordenes/")
async def mostrar_ordenes():
    ordenes = []
    for pedido in restaurante.mostrar_ordenes():
        ordenes.append({str(pedido)})
    return {"ordenes": ordenes}

@router.get("/menu/")
async def mostrar_menu():
    menu = restaurante.mostrar_menu()
    return {"menu": menu}
