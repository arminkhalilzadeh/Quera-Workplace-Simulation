from workplace_sim.workplaces.work_place import Consts, WorkPlace


class Mine(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "mine"
        self.calc_capacity()

    def calc_capacity(self) -> None:
        self.capacity = self.level**2

    def calc_costs(self) -> int:
        return Consts.BASE_PLACE_COST + Consts.LEVEL_MUL * self.level
