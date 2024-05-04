# Subsistema 1
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

# Subsistema 2
class Lights:
    def turn_on(self):
        print("Lights turned on")

    def turn_off(self):
        print("Lights turned off")

# Subsistema 3
class AirConditioner:
    def start(self):
        print("Air conditioner started")

    def stop(self):
        print("Air conditioner stopped")

# Fachada
class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.lights = Lights()
        self.air_conditioner = AirConditioner()

    def start_car(self):
        self.engine.start()
        self.lights.turn_on()
        self.air_conditioner.start()

    def stop_car(self):
        self.engine.stop()
        self.lights.turn_off()
        self.air_conditioner.stop()

# Cliente
if __name__ == "__main__":
    car = CarFacade()

    # Encender el coche usando la fachada
    car.start_car()

    # Apagar el coche usando la fachada
    car.stop_car()
