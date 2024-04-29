from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def get_best_route(self, origin: int, destination: int) -> dict:
        pass

    @abstractmethod
    def get_cost(self, origin: int, destination: int) -> float:
        pass

    @abstractmethod
    def get_time(self, origin: int, destination: int) -> float:
        pass


class CarRoute(RouteStrategy):
    def get_best_route(self, origin: int, destination: int) -> dict:
        return {"start_street": origin, "end_street": destination, "route": "Use the avenue 123"}

    def get_cost(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.1, 2)

    def get_time(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.5, 2)


class BikeRoute(RouteStrategy):
    def get_best_route(self, origin: int, destination: int) -> dict:
        return {"start_street": origin, "end_street": destination, "route": "Use the bike lane"}

    def get_cost(self, origin: int, destination: int) -> float:
        return 0

    def get_time(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 2, 2)


class MotorcycleRoute(RouteStrategy):
    def get_best_route(self, origin: int, destination: int) -> dict:
        return {"start_street": origin, "end_street": destination, "route": "Use the motorcycle lane"}

    def get_cost(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.05, 2)

    def get_time(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.25, 2)


class DroneRoute(RouteStrategy):
    def get_best_route(self, origin: int, destination: int) -> dict:
        return {"start_street": origin, "end_street": destination, "route": "Use the air route"}

    def get_cost(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.01, 2)

    def get_time(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.1, 2)
