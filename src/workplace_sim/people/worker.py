from workplace_sim.people.person import Consts, Person


class Worker(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.job = "worker"

    def get_price(self) -> int:
        return int(Consts.BASE_PRICE["worker"] * Consts.MIN_AGE / self.age)

    def calc_life_cost(self) -> int:
        return int(Consts.BASE_COST["worker"] * self.age / Consts.MIN_AGE)

    def calc_income(self) -> int:
        return int(Consts.BASE_INCOME["worker"]["mine"] * Consts.MIN_AGE / self.age)
