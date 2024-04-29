from enum import Enum

from fastapi import APIRouter, Depends

from .strategy import BikeRoute, CarRoute, DroneRoute, MotorcycleRoute, RouteStrategy


class Vehicle(Enum):
    CAR = "car"
    BIKE = "bike"
    MOTORCYCLE = "motorcycle"
    DRONE = "drone"


def get_strategy(vehicle: Vehicle) -> RouteStrategy:
    defined_vehicles = {
        Vehicle.CAR: CarRoute(),
        Vehicle.BIKE: BikeRoute(),
        Vehicle.MOTORCYCLE: MotorcycleRoute(),
        Vehicle.DRONE: DroneRoute(),
    }
    return defined_vehicles[vehicle]


router = APIRouter()


@router.get("/best_route")
def best_route(origin: int, destination: int, vehicle: RouteStrategy = Depends(get_strategy)) -> dict:
    return vehicle.get_best_route(origin=origin, destination=destination)


@router.get("/cost")
def cost(origin: int, destination: int, vehicle: RouteStrategy = Depends(get_strategy)) -> float:
    return vehicle.get_cost(origin=origin, destination=destination)


@router.get("/time")
def time(origin: int, destination: int, vehicle: RouteStrategy = Depends(get_strategy)) -> float:
    return vehicle.get_time(origin=origin, destination=destination)
