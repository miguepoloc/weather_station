from fastapi import FastAPI, HTTPException, Depends, status
from typing import List

app = FastAPI()

# Simulación de base de datos de tickets disponibles
available_tickets = {
    "Londres": 10,
    "París": 5,
    "Nueva York": 8
}

# Decorador para verificar la disponibilidad de los tickets
def check_ticket_availability(func):
    def wrapper(destination: str, tickets_requested: int, *args, **kwargs):
        if destination in available_tickets and available_tickets[destination] >= tickets_requested:
            return func(destination, tickets_requested, *args, **kwargs)
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"No hay suficientes tickets disponibles para {destination}"
            )
    return wrapper

# Ruta protegida por el decorador
@app.get("/comprar_tickets_decorator")
@check_ticket_availability
def comprar_tickets(destination: str, tickets_requested: int):
    # Simulación de compra exitosa
    return {"message": f"¡Compra exitosa! Se han comprado {tickets_requested} tickets para {destination}"}

# Ejemplo de consumo del endpoint
@app.get("/")
def home():
    return {"message": "Bienvenido al servicio de venta de tickets aéreos"}