from person import Person, Consts
import math


class Teacher(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.job = "teacher"

    def get_price(self) -> int:
        price = Consts.BASE_PRICE['teacher'] - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL
        return price
    
    def calc_life_cost(self) -> int:
        costs = Consts.BASE_COST['teacher'] + (self.age - Consts.MIN_AGE) * Consts.AGE_MUL
        return costs

    def calc_income(self) -> int:
        income = Consts.BASE_INCOME['teacher']['school'] - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL
        return int(income)