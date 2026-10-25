from __future__ import annotations

import math
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from workplace_sim.workplaces.work_place import WorkPlace


class Consts:
    BASE_PRICE = {"worker": 1200, "teacher": 1500, "engineer": 2000}
    BASE_COST = {"worker": 200, "teacher": 150, "engineer": 300}
    BASE_INCOME = {"worker": {"mine": 800}, "teacher": {"school": 300}, "engineer": {"company": 1000}}
    MIN_AGE = 15
    AGE_MUL = 10


class Person(ABC):
    """Base class for every citizen. Subclasses define the job-specific economics."""

    instances: ClassVar[list[Person]] = []

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.level = 1
        self.job = ""
        self.work_place: WorkPlace | None = None
        Person.instances.append(self)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r}, age={self.age}, level={self.level})"

    @abstractmethod
    def get_price(self) -> int:
        """Cost of training a person for this job."""

    @abstractmethod
    def calc_income(self) -> int:
        """Daily base income before level adjustment."""

    @abstractmethod
    def calc_life_cost(self) -> int:
        """Daily cost of living."""

    def do_level(self, income: float) -> float:
        """Scale income by the geometric mean of the person's and the workplace's level."""
        if self.work_place is None:
            return 0.0
        return income * math.sqrt(self.level * self.work_place.level)

    def calc(self) -> float:
        """Daily net balance: level-adjusted income minus cost of living."""
        income = self.calc_income() if self.work_place is not None else 0
        return self.do_level(income) - self.calc_life_cost()

    def get_job(self) -> str:
        return self.job

    def upgrade(self) -> None:
        self.level += 1

    @staticmethod
    def calc_all() -> float:
        """Total daily net balance of all people."""
        return sum(person.calc() for person in Person.instances)
