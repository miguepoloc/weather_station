from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class MensajeroImplementador:
    def enviar_mensaje(self, mensaje):
        pass


class MensajeroEmail(MensajeroImplementador):
    def enviar_mensaje(self, mensaje):
        print("Enviando mensaje por correo electrónico:", mensaje)

class MensajeroSMS(MensajeroImplementador):
    def enviar_mensaje(self, mensaje):
        print("Enviando mensaje por SMS:", mensaje)

class MensajeroPush(MensajeroImplementador):
    def enviar_mensaje(self, mensaje):
        print("Enviando mensaje por notificación push:", mensaje)


class Mensajero:
    def __init__(self, implementador):
        self._implementador = implementador

    def enviar(self, mensaje):
        self._implementador.enviar_mensaje(mensaje)


class MensajeroUrgente(Mensajero):
    def enviar(self, mensaje):
        mensaje = "[Urgente] " + mensaje
        super().enviar(mensaje)

class MensajeroNormal(Mensajero):
    pass
