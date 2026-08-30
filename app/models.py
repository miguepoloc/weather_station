"""Modelos SQLAlchemy.

Nota para la clase: se simplificaron los campos de sensor del proyecto IoT original (temperatura,
humedad, presión, batería) para que el código quepa en una diapositiva sin ruido — el dominio real
tenía 13 campos (suelo, HD38, etc.) que no aportan nada a entender los patrones.
"""

from __future__ import annotations

import datetime
import enum
from typing import Any

import sqlalchemy
from sqlalchemy import orm

Base: Any = orm.declarative_base()


class NodeType(str, enum.Enum):
    MASTER = "master"
    WORKER = "worker"


class Node(Base):
    __tablename__ = "nodes"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    type = sqlalchemy.Column(sqlalchemy.Enum(NodeType), nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    latitude = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    longitude = sqlalchemy.Column(sqlalchemy.Float, nullable=False)

    readings = orm.relationship("SensorReading", backref="node")


class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    node_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("nodes.id"), nullable=False)
    date_time = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow)

    temperature = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    humidity = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    pressure = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    battery_level = sqlalchemy.Column(sqlalchemy.Float, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    email = sqlalchemy.Column(sqlalchemy.String(255), unique=True, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    first_name = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    last_name = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
