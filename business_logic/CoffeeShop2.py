from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class CoffeeShop2:
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")

    def switch(self, part, currentPoints):
        if part == "PartA1":
            return currentPoints * 2
        if part == "PartB1":
            return currentPoints + 3
        if part == "PartC1":
            return currentPoints * 5

        return 0

    def computePointsScheme(self, currentBalance) -> int:
        for part in self.parts:
            currentBalance += self.switch(part, currentBalance)

        return currentBalance