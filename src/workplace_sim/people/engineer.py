import math

from workplace_sim.people.person import Consts, Person


class Engineer(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.job = "engineer"

    def get_price(self) -> int:
        return int(Consts.BASE_PRICE["engineer"] * math.sqrt(Consts.MIN_AGE / self.age))

    def calc_life_cost(self) -> int:
        return int(Consts.BASE_COST["engineer"] * math.sqrt(self.age / Consts.MIN_AGE))

    def calc_income(self) -> int:
        return int(Consts.BASE_INCOME["engineer"]["company"] * math.sqrt(Consts.MIN_AGE / self.age))
