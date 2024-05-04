from fastapi import APIRouter, HTTPException
from src2.decorators import validate_reservation_date, check_availability

router = APIRouter()

@router.post("/reserve/")
def reserve_room(room_type: str, date: str, num_students: int):
    # Lógica para reservar el salón
    return reserve_room_logic(room_type, date, num_students)

@router.post("/cancel/")
def cancel_reservation(room_id: int):
    # Lógica para cancelar la reserva
    return {"message": f"Reservation for room ID {room_id} canceled successfully"}

#@validate_reservation_date
@check_availability
def reserve_room_logic(room_type: str, date: str, num_students: int):
    # Lógica para reservar el salón
    return {"message": f"Room of type {room_type} reserved for {date} for {num_students} students"}