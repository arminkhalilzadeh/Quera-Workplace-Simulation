from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from workplace_sim.people.person import Person


class WorkPlaceIsFull(Exception):
    def __str__(self) -> str:
        return "work place is full!"


class Consts:
    BASE_PRICE = {"mine": 150, "school": 100, "company": 90}
    BASE_PLACE_COST = 2500
    LEVEL_MUL = 50


class WorkPlace(ABC):
    """Base class for workplaces. Subclasses define capacity and maintenance cost per level."""

    instances: ClassVar[list[WorkPlace]] = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees: list[Person] = []
        self.capacity = 1
        WorkPlace.instances.append(self)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r}, level={self.level}, capacity={self.capacity})"

    @abstractmethod
    def calc_capacity(self) -> None:
        """Update ``self.capacity`` for the current level."""

    @abstractmethod
    def calc_costs(self) -> int:
        """Daily maintenance cost."""

    def get_price(self) -> int:
        return Consts.BASE_PRICE[self.expertise]

    def get_expertise(self) -> str:
        return self.expertise

    def upgrade(self) -> None:
        self.level += 1
        self.calc_capacity()

    def hire(self, person: Person) -> None:
        if len(self.employees) >= self.capacity:
            raise WorkPlaceIsFull()
        self.employees.append(person)
        person.work_place = self

    def calc(self) -> int:
        """Daily net balance of the workplace (its maintenance cost, as a negative number)."""
        return -self.calc_costs()

    @staticmethod
    def calc_all() -> int:
        """Total daily net balance of all workplaces."""
        return sum(work_place.calc() for work_place in WorkPlace.instances)
