from fastapi import HTTPException

def validate_reservation_date(func):
    def wrapper(date):
        if not date:
            raise HTTPException(status_code=400, detail="Date is required for reservation")
        return func(date)
    return wrapper

def check_availability(func):
    def wrapper(room_type, date, num_students):
        if room_type == "clases" and num_students > 50:
            raise HTTPException(status_code=400, detail="Cannot reserve classroom for more than 50 students")
        elif room_type == "laboratorio" and num_students > 20:
            raise HTTPException(status_code=400, detail="Cannot reserve laboratory for more than 20 students")
        elif room_type == "biblioteca" and num_students > 100:
            raise HTTPException(status_code=400, detail="Cannot reserve library for more than 100 students")
        return func(room_type,date, num_students)
    return wrapper

# Ejemplo de uso de los decoradores

# Función para reservar un salón
@validate_reservation_date
@check_availability
def reserve_room(room_type: str, date: str, num_students: int):
    # Aquí iría la lógica para reservar el salón
    return {"message": f"Room of type {room_type} reserved for {date} for {num_students} students"}