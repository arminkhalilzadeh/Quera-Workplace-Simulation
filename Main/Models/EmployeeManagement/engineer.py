from person import Person, Consts
import math


class Engineer(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.job = "engineer"

    def get_price(self) -> int:
        price = int(Consts.BASE_PRICE['engineer'] * (math.sqrt(Consts.MIN_AGE / self.age)))
        return price
    
    def calc_life_cost(self) -> int:
        costs = int(Consts.BASE_COST['engineer'] *(math.sqrt (self.age / Consts.MIN_AGE)))
        return costs

    def calc_income(self) -> int:
        income = int(Consts.BASE_INCOME['engineer']['company'] * (math.sqrt(Consts.MIN_AGE / self.age)))
        return int(income)