from abc import ABC, abstractmethod

class EstadoAutomovil(ABC):
    @abstractmethod
    def get_state(self, motor: str, llantas: str, aceite : str, batería: bool ) -> str:
        pass


class Funcional(EstadoAutomovil):
    def get_state(self):
        return "El automóvil está funcional."


class Averiado(EstadoAutomovil):
    def get_state(self, motor: str, llantas: str, aceite : str, batería: bool ) -> str:
        if  motor == 'averiado' or llantas == 'funcional' or aceite == 'bajo' and batería == False:
            return "El automóvil está averiado."
        else:
            return "El automóvil está funcional."


class Mantenimiento(EstadoAutomovil):
    def get_state(self, motor: str, llantas: str, aceite : str, batería: bool ) -> str:
        if motor == 'funcional' or llantas == 'desgastadas' or aceite == 'bajo' and batería == True:
            return "El automóvil está averiado."
        else:
            return "El automóvil está en mantenimiento."


class InterfaceAutomovil:
    def __init__(self, estado):
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def obtener_estado(self):
        return self.estado.get_state()

def get_estado(self):
        get: dict = automovil.estado.get(
            {
                "motor": "funcional",
                "llantas": "averiado",
                "aceite": "bajo",
                "batería": False,
            }
        )
        return get

if __name__ == "__main__":
    #instancias
    funcional = Funcional()
    averiado = Averiado()
    mantenimiento = Mantenimiento()


    automovil = InterfaceAutomovil(funcional)


    print(automovil.obtener_estado())


    automovil.cambiar_estado(averiado)
    print(automovil.obtener_estado())


    automovil.cambiar_estado(mantenimiento)
    print(automovil.obtener_estado())
