from workplace_sim.people.person import Consts, Person


class Teacher(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.job = "teacher"

    def get_price(self) -> int:
        return Consts.BASE_PRICE["teacher"] - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL

    def calc_life_cost(self) -> int:
        return Consts.BASE_COST["teacher"] + (self.age - Consts.MIN_AGE) * Consts.AGE_MUL

    def calc_income(self) -> int:
        return Consts.BASE_INCOME["teacher"]["school"] - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL
