from pydantic import BaseModel
from typing import List

class Pizza(BaseModel):
    size: str
    cheese: bool = False
    pepperoni: bool = False
    mushrooms: bool = False
    extra_toppings: List[str] = []


class PizzaBuilderInterface:
    def set_size(self, size: str):
        pass

    def add_cheese(self):
        pass

    def add_pepperoni(self):
        pass

    def add_mushrooms(self):
        pass

    def add_topping(self, topping: str):
        pass

    def build(self) -> Pizza:
        pass


class PizzaBuilder(PizzaBuilderInterface):
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size: str):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_topping(self, topping: str):
        self.pizza.extra_toppings.append(topping)
        return self

    def build(self) -> Pizza:
        return self.pizza
