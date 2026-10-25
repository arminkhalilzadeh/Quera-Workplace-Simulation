from workplace_sim.workplaces.work_place import Consts, WorkPlace


class Company(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "company"
        self.calc_capacity()

    def calc_capacity(self) -> None:
        self.capacity = self.level

    def calc_costs(self) -> int:
        return Consts.BASE_PLACE_COST * self.level
