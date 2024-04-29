from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Any

Base: Any = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)

    def save(self):
        if self.is_active:
            self.deleted_at = None
        else:
            self.deleted_at = datetime.now()
        super().save()

    def update(self, *args, **kwargs):
        if self.is_active:
            self.deleted_at = None
        else:
            self.deleted_at = datetime.now()
        super().update(*args, **kwargs)


class NodeType(Enum):
    MASTER = 'master'
    WORKER = 'worker'


class Nodes(BaseModel):
    __tablename__ = 'nodes'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    type = Column(Enum(NodeType.MASTER, NodeType.WORKER), nullable=False)  # type: ignore
    description = Column(String, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    storages = relationship('NodesStorage', backref='node')


class NodesStorage(BaseModel):
    __tablename__: str = 'nodes_storage'

    id = Column(Integer, primary_key=True)
    node_id = Column(Integer, ForeignKey('nodes.id'), nullable=False)
    date_time = Column(DateTime, default=func.now())
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    altitude = Column(Float, nullable=False)
    humidity_hd38 = Column(Float, nullable=False)
    humidity_soil = Column(Float, nullable=False)
    temperature_soil = Column(Float, nullable=False)
    conductivity_soil = Column(Float, nullable=False)
    ph_soil = Column(Float, nullable=False)
    nitrogen_soil = Column(Float, nullable=False)
    phosphorus_soil = Column(Float, nullable=False)
    potassium_soil = Column(Float, nullable=False)
    battery_level = Column(Float, nullable=False)
    temperature_soil = Column(Float, nullable=False)
    conductivity_soil = Column(Float, nullable=False)
    ph_soil = Column(Float, nullable=False)
    nitrogen_soil = Column(Float, nullable=False)
    phosphorus_soil = Column(Float, nullable=False)
    potassium_soil = Column(Float, nullable=False)
    battery_level = Column(Float, nullable=False)
