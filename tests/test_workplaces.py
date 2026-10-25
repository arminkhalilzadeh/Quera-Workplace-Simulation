import math

import pytest

from workplace_sim import Company, Mine, School, Worker, WorkPlace, WorkPlaceIsFull
from workplace_sim.workplaces import Consts


def test_workplace_is_abstract():
    with pytest.raises(TypeError):
        WorkPlace("generic")


@pytest.mark.parametrize("cls, expertise", [(Mine, "mine"), (School, "school"), (Company, "company")])
def test_constructor(cls, expertise):
    place = cls("Quera")
    assert (place.name, place.level, place.capacity, place.employees) == ("Quera", 1, 1, [])
    assert place.get_expertise() == expertise
    assert place.get_price() == Consts.BASE_PRICE[expertise]


def test_mine_capacity_and_costs():
    mine = Mine("Kerman")
    mine.level = 10
    mine.calc_capacity()
    assert mine.capacity == 100
    assert mine.calc_costs() == Consts.BASE_PLACE_COST + Consts.LEVEL_MUL * 10


def test_school_capacity_and_costs():
    school = School("Akhlagh")
    school.level = 123
    school.calc_capacity()
    assert school.capacity == 11
    assert school.calc_costs() == Consts.BASE_PLACE_COST * int(math.sqrt(123))


def test_company_capacity_and_costs():
    company = Company("Quera")
    company.level = 10
    company.calc_capacity()
    assert company.capacity == 10
    assert company.calc_costs() == Consts.BASE_PLACE_COST * 10


def test_upgrade_recomputes_capacity():
    mine = Mine("Kerman")
    mine.upgrade()
    assert (mine.level, mine.capacity) == (2, 4)


def test_hire_links_both_sides():
    mine = Mine("Kerman")
    worker = Worker("Amir", 18)
    mine.hire(worker)
    assert mine.employees == [worker]
    assert worker.work_place is mine


def test_hire_beyond_capacity_raises():
    company = Company("Quera")
    company.hire(Worker("Amir", 18))
    with pytest.raises(WorkPlaceIsFull, match="work place is full!"):
        company.hire(Worker("Sara", 20))


def test_calc_is_negative_maintenance_cost():
    company = Company("Quera")
    assert company.calc() == -company.calc_costs()


def test_calc_all_sums_every_workplace():
    places = [Mine("Kerman"), School("Akhlagh"), Company("Quera")]
    assert WorkPlace.calc_all() == sum(p.calc() for p in places)
