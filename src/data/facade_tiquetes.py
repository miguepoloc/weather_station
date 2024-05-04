from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# Simulación de base de datos de tickets disponibles
available_tickets = {
    "Londres": 10,
    "París": 5,
    "Nueva York": 8
}

class TicketService:
    @staticmethod
    def check_ticket_availability(destination: str, tickets_requested: int):
        if destination in available_tickets and available_tickets[destination] >= tickets_requested:
            return True
        else:
            return False

    @staticmethod
    def buy_tickets(destination: str, tickets_requested: int):
        if TicketService.check_ticket_availability(destination, tickets_requested):
            # Simulación de compra exitosa
            return {"message": f"¡Compra exitosa! Se han comprado {tickets_requested} tickets para {destination}"}
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"No hay suficientes tickets disponibles para {destination}"
            )

ticket_service = TicketService()

# Ruta protegida por el patrón Facade
@app.get("/comprar_tickets_facade")
def comprar_tickets_facade(destination: str, tickets_requested: int):
    return ticket_service.buy_tickets(destination, tickets_requested)

# Ejemplo de consumo del endpoint
@app.get("/")
def home():
    return {"message": "Bienvenido al servicio de venta de tickets aéreos"}