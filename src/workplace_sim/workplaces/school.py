import math

from workplace_sim.workplaces.work_place import Consts, WorkPlace


class School(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "school"
        self.calc_capacity()

    def calc_capacity(self) -> None:
        self.capacity = math.isqrt(self.level)

    def calc_costs(self) -> int:
        return Consts.BASE_PLACE_COST * math.isqrt(self.level)
