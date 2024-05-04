from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime

from src.models import NodesStorage
from src.send_email import send_email


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: NodeSubject) -> None:
        """
        Receive update from subject.
        """
        pass


class NodeSubject:
    def __init__(self, node: NodesStorage) -> None:
        self.node: NodesStorage = node
        self.__observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self)

    def check_battery(self) -> None:
        if self.node.battery_level < 10:
            self.notify()


class ConsoleObserver(Observer):
    def update(self, subject: NodeSubject) -> None:
        print(f"La batería del nodo está baja: {subject.node.battery_level} voltios")


class EmailObserver(Observer):
    def update(self, subject: NodeSubject) -> None:
        message_html: str = f"""<b>La batería del nodo {subject.node.node_id} está baja</b>
        <br>
        <p>Batería: {subject.node.battery_level} voltios</p>
        <br>
        <p>Fecha: {datetime.now()}</p>
        <br>
        <p>Nodo: {subject.node.node_id}</p>
        <br>
        <p>
        """
        send_email(
            to_email=["miguepoloc@gmail.com"],
            subject=f"La batería del nodo {subject.node.node_id} está baja",
            html=message_html,
        )


class SmsObserver(Observer):
    def update(self, subject: NodeSubject) -> None:
        print(f"Enviando SMS: La batería del nodo está baja: {subject.node.battery_level} voltios")
