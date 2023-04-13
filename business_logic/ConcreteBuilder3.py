from __future__ import annotations
from CoffeeShop3 import CoffeeShop3
from CoffeeShopBuilder import CoffeeShopBuilder
from abc import ABC, abstractmethod
from typing import Any


class ConcreteBuilder3(CoffeeShopBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self._product = None
        self.reset()

    def reset(self) -> None:
        self._product = CoffeeShop3()

    @property
    def product(self) -> CoffeeShop3:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")

    def produce_part_d(self) -> None:
        self._product.add("PartD1")
