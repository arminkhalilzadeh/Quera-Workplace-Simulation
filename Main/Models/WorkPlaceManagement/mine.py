from work_place import WorkPlace, Consts
import math


class Mine(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "mine"

    def calc_capacity(self) -> None:
        self.capacity = int((self.level ** 2))

    def calc_costs(self) -> int:
        costs = Consts.BASE_PLACE_COST + (Consts.LEVEL_MUL * self.level)
        return costs
