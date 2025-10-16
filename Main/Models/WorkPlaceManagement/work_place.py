class WorkPlaceIsFull(Exception):
    def __str__(self):
        return "work place is full!"


class Consts:
    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}
    BASE_PLACE_COST = 2500
    LEVEL_MUL = 50


class WorkPlace:
    instances = list()
    def __init__(self, name: str) -> None:
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = list()
        self.capacity = 1

        WorkPlace.instances.append(self)

    def get_price(self) -> int:
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self) -> None:
        self.level += 1
        self.calc_capacity()

    def hire(self, person) -> None:
        if self.capacity <= len(self.employees):
            raise WorkPlaceIsFull()
        else:
            self.employees.append(person)
            person.work_place = self

    def get_expertise(self) -> str:
        return self.expertise

    def calc(self) -> int:
        return -(self.calc_costs())

    @staticmethod
    def calc_all() -> int:
        total_cost = 0
        for work_place in WorkPlace.instances:
            total_cost += WorkPlace.calc(work_place)
        return total_cost

