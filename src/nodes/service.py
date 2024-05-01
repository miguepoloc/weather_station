from abc import ABC, abstractmethod
from itertools import groupby
from operator import attrgetter
from typing import Optional

from nodes.schemas import NodesStorageModel, NodeType


class NodesDataStrategy(ABC):
    @abstractmethod
    def get_nodes_data(self, data: list[NodesStorageModel]) -> list[NodesStorageModel]:
        pass


class TotalNodesData(NodesDataStrategy):
    def get_nodes_data(self, data: list[NodesStorageModel]) -> list[NodesStorageModel]:
        return data


class HoursNodesData(NodesDataStrategy):
    def get_nodes_data(self, data: list[NodesStorageModel]) -> list[NodesStorageModel]:
        for d in data:
            d.hour = d.date_time.hour

        data.sort(key=attrgetter('hour'))
        grouped_data = groupby(data, key=attrgetter('hour'))

        averaged_data: list = []
        for hour, group in grouped_data:
            group_list = list(group)
            averaged_node = NodesStorageModel(
                id=group_list[0].id,
                node_id=group_list[0].node_id,
                date_time=group_list[0].date_time,
                hour=hour,
                temperature=sum(d.temperature for d in group_list) / len(group_list),
                humidity=sum(d.humidity for d in group_list) / len(group_list),
                pressure=sum(d.pressure for d in group_list) / len(group_list),
                altitude=sum(d.altitude for d in group_list) / len(group_list),
                humidity_hd38=sum(d.humidity_hd38 for d in group_list) / len(group_list),
                humidity_soil=sum(d.humidity_soil for d in group_list) / len(group_list),
                temperature_soil=sum(d.temperature_soil for d in group_list) / len(group_list),
                conductivity_soil=sum(d.conductivity_soil for d in group_list) / len(group_list),
                ph_soil=sum(d.ph_soil for d in group_list) / len(group_list),
                nitrogen_soil=sum(d.nitrogen_soil for d in group_list) / len(group_list),
                phosphorus_soil=sum(d.phosphorus_soil for d in group_list) / len(group_list),
                potassium_soil=sum(d.potassium_soil for d in group_list) / len(group_list),
                battery_level=sum(d.battery_level for d in group_list) / len(group_list),
            )
            averaged_data.append(averaged_node)

        return averaged_data


class DaysNodesData(NodesDataStrategy):
    def get_nodes_data(self, data: list[NodesStorageModel]) -> list[NodesStorageModel]:
        # Add the date to each element of data with out the hour
        for d in data:
            d.date = d.date_time.date()

        data.sort(key=attrgetter('date'))
        grouped_data = groupby(data, key=attrgetter('date'))

        averaged_data: list = []
        for date, group in grouped_data:
            group_list = list(group)
            averaged_node = NodesStorageModel(
                id=group_list[0].id,
                node_id=group_list[0].node_id,
                date_time=group_list[0].date_time,
                date=date,
                temperature=sum(d.temperature for d in group_list) / len(group_list),
                humidity=sum(d.humidity for d in group_list) / len(group_list),
                pressure=sum(d.pressure for d in group_list) / len(group_list),
                altitude=sum(d.altitude for d in group_list) / len(group_list),
                humidity_hd38=sum(d.humidity_hd38 for d in group_list) / len(group_list),
                humidity_soil=sum(d.humidity_soil for d in group_list) / len(group_list),
                temperature_soil=sum(d.temperature_soil for d in group_list) / len(group_list),
                conductivity_soil=sum(d.conductivity_soil for d in group_list) / len(group_list),
                ph_soil=sum(d.ph_soil for d in group_list) / len(group_list),
                nitrogen_soil=sum(d.nitrogen_soil for d in group_list) / len(group_list),
                phosphorus_soil=sum(d.phosphorus_soil for d in group_list) / len(group_list),
                potassium_soil=sum(d.potassium_soil for d in group_list) / len(group_list),
                battery_level=sum(d.battery_level for d in group_list) / len(group_list),
            )
            averaged_data.append(averaged_node)

        return averaged_data


class NodeCreation(ABC):
    @abstractmethod
    def __init__(self, name: str, description: Optional[str], latitude: float, longitude: float) -> None:
        self.name: str = name
        self.description: str | None = description
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.type: NodeType


class NodeFather(NodeCreation):
    def __init__(self, name: str, description: Optional[str], latitude: float, longitude: float):
        super().__init__(name=name, description=description, latitude=latitude, longitude=longitude)
        self.type = NodeType.MASTER


class NodeChild(NodeCreation):
    def __init__(self, name: str, description: Optional[str], latitude: float, longitude: float):
        super().__init__(name=name, description=description, latitude=latitude, longitude=longitude)
        self.type = NodeType.WORKER


class NodoFactory:
    @staticmethod
    def create_node(
        type_node: NodeType, name: str, description: Optional[str], latitude: float, longitude: float
    ) -> NodeCreation:
        if type_node == NodeType.MASTER:
            return NodeFather(name=name, description=description, latitude=latitude, longitude=longitude)
        elif type_node == NodeType.WORKER:
            return NodeChild(name=name, description=description, latitude=latitude, longitude=longitude)
        else:
            raise ValueError(f"Invalid type {type_node} to create node")
