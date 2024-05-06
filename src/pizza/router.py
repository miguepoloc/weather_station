from fastapi import APIRouter
from builder import PizzaBuilder
from pydantic import BaseModel
from typing import List
from enum import Enum

# Acá validando y serializamos con BaseModel de pydantic para fastAPI
class Pizza(BaseModel):
    size: str
    cheese: bool = False
    pepperoni: bool = False
    mushrooms: bool = False
    extra_toppings: List[str] = []


#Usamos Enum para evitar tantos If dentro del método POST
class PizzaSize(str, Enum):
    small = "small"
    medium = "medium"
    large = "large"


class PizzaAttribute(Enum):
    cheese = "add_cheese"
    pepperoni = "add_pepperoni"
    mushrooms = "add_mushrooms"



router = APIRouter()

@router.post("/build-pizza-builder/")
async def build_pizza_builder(size: PizzaSize, attributes: List[PizzaAttribute], extra_toppings: List[str] = []):
    builder = PizzaBuilder()
    builder.set_size(size.value)

    for attribute in attributes:
        getattr(builder, attribute.value)()

    for topping in extra_toppings:
        builder.add_topping(topping)

    pizza = builder.build()
    return pizza