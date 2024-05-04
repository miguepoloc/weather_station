class Manejador:
    def __init__(self, sucesor=None):
        self._sucesor = sucesor

    def manejar_solicitud(self, solicitud):
        pass

class ManejadorDescuento(Manejador):
    def manejar_solicitud(self, solicitud):
        if solicitud['tipo_cliente'] == 'nuevo_cliente':
            return self.descuento_nuevo_cliente(solicitud['monto'])
        elif self._sucesor:
            return self._sucesor.manejar_solicitud(solicitud)
        else:
            return 0

    def descuento_nuevo_cliente(self, monto):
        return monto * 0.10

class ManejadorPremium(Manejador):
    def manejar_solicitud(self, solicitud):
        if solicitud['tipo_cliente'] == 'premium':
            return self.descuento_premium(solicitud['monto'])
        elif self._sucesor:
            return self._sucesor.manejar_solicitud(solicitud)
        else:
            return 0

    def descuento_premium(self, monto):
        return monto * 0.20

class ManejadorVIP(Manejador):
    def manejar_solicitud(self, solicitud):
        if solicitud['tipo_cliente'] == 'vip':
            return self.descuento_vip(solicitud['monto'])
        elif self._sucesor:
            return self._sucesor.manejar_solicitud(solicitud)
        else:
            return 0

    def descuento_vip(self, monto):
        return monto * 0.30

# Uso del patrón
if __name__ == "__main__":
    manejador_vip = ManejadorVIP()
    manejador_premium = ManejadorPremium(manejador_vip)
    manejador_descuento = ManejadorDescuento(manejador_premium)

    solicitudes = [
        {'tipo_cliente': 'nuevo_cliente', 'monto': 100},
        {'tipo_cliente': 'premium', 'monto': 200},
        {'tipo_cliente': 'vip', 'monto': 300},
        {'tipo_cliente': 'regular', 'monto': 400}
    ]

    for solicitud in solicitudes:
        descuento = manejador_descuento.manejar_solicitud(solicitud)
        print(f"Para el cliente {solicitud['tipo_cliente']}, el descuento aplicado es: {descuento}")