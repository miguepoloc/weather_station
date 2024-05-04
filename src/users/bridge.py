from abc import ABC, abstractmethod

class InterfaceAutomovil(ABC):
    def __init__(self, estado):
        self._estado = estado

    def cambiar_estado(self, nuevo_estado):
        self._estado = nuevo_estado

    @abstractmethod
    def obtener_estado(self):
        pass


class EstadoAutomovil(ABC):
    @abstractmethod
    def get_state(self, motor: str, llantas: str, aceite: str, bateria: bool) -> dict:
        pass


class EstadoConcreto(EstadoAutomovil):
    def get_state(self, motor: str, llantas: str, aceite: str, bateria: bool) -> dict:
        return "El automóvil está funcional."

class Funcional(EstadoAutomovil):
    def get_state(self, motor: str, llantas: str, aceite: str, bateria: bool) -> dict:
        return "El automóvil está funcional."

class Averiado(EstadoAutomovil):
    def get_state(self, motor: str, llantas: str, aceite: str, bateria: bool) -> dict:
        if motor == 'averiado' or llantas == 'funcional' or aceite == 'bajo' and not bateria:
            return "El automóvil está averiado."
        else:
            return "El automóvil está funcional."

class Mantenimiento(EstadoAutomovil):
    def get_state(self, motor: str, llantas: str, aceite: str, bateria: bool) -> dict:
        if motor == 'funcional' or llantas == 'desgastadas' or aceite == 'bajo' and bateria:
            return "El automóvil está en mantenimiento."
        else:
            return "El automóvil está funcional."


class InterfaceAutomovilRefinada(InterfaceAutomovil):
    def __init__(self, estado: EstadoAutomovil):
        self._estado = estado

    def obtener_estado(self, motor: str, llantas: str, aceite: str, bateria: bool) -> dict:
        return self._estado.get_state(motor, llantas, aceite, bateria)


if __name__ == "__main__":

    funcional = Funcional()
    averiado = Averiado()
    mantenimiento = Mantenimiento()


    automovil_funcional = InterfaceAutomovilRefinada(funcional)
    automovil_averiado = InterfaceAutomovilRefinada(averiado)
    automovil_mantenimiento = InterfaceAutomovilRefinada(mantenimiento)


    print(automovil_funcional.obtener_estado('funcional', 'funcional', 'funcional', True))
    print(automovil_averiado.obtener_estado('averiado', 'funcional', 'bajo', False))
    print(automovil_mantenimiento.obtener_estado('funcional', 'funcional', 'funcional', True))
