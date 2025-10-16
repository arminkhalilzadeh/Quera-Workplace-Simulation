from person import Person, Consts
import math


class Worker(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.job = "worker"

    def get_price(self) -> int:
        price = int(Consts.BASE_PRICE['worker'] * Consts.MIN_AGE / self.age)
        return price

    def calc_life_cost(self) -> int:
        costs = int(Consts.BASE_COST['worker'] * self.age / Consts.MIN_AGE)
        return costs

    def calc_income(self) -> int:
        income = int(Consts.BASE_INCOME['worker']['mine'] * Consts.MIN_AGE / self.age)
        return income