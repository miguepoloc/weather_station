"""Modelos SQLAlchemy.

Nota para la clase: se simplificaron los campos de sensor del proyecto IoT original (temperatura,
humedad, presión, batería) para que el código quepa en una diapositiva sin ruido — el dominio real
tenía 13 campos (suelo, HD38, etc.) que no aportan nada a entender los patrones.
"""

from __future__ import annotations

import enum
from datetime import datetime
from typing import Any

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base: Any = declarative_base()


class NodeType(str, enum.Enum):
    MASTER = "master"
    WORKER = "worker"


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    type = Column(Enum(NodeType), nullable=False)
    description = Column(String, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    readings = relationship("SensorReading", backref="node")


class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True)
    node_id = Column(Integer, ForeignKey("nodes.id"), nullable=False)
    date_time = Column(DateTime, default=datetime.utcnow)

    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    battery_level = Column(Float, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
