import math

import pytest

from workplace_sim import Company, Engineer, Mine, Person, School, Teacher, Worker
from workplace_sim.people import Consts


@pytest.mark.parametrize("cls, job", [(Worker, "worker"), (Teacher, "teacher"), (Engineer, "engineer")])
def test_constructor(cls, job):
    person = cls("Sara", 20)
    assert (person.name, person.age, person.level, person.job) == ("Sara", 20, 1, job)
    assert person.work_place is None
    assert person.get_job() == job


def test_person_is_abstract():
    with pytest.raises(TypeError):
        Person("Ali", 20)


def test_worker_economics():
    worker = Worker("Amir", 18)
    assert worker.get_price() == int(Consts.BASE_PRICE["worker"] * Consts.MIN_AGE / 18)
    assert worker.calc_life_cost() == int(Consts.BASE_COST["worker"] * 18 / Consts.MIN_AGE)
    assert worker.calc_income() == int(Consts.BASE_INCOME["worker"]["mine"] * Consts.MIN_AGE / 18)


def test_teacher_economics():
    teacher = Teacher("Niloo", 19)
    assert teacher.get_price() == Consts.BASE_PRICE["teacher"] - 4 * Consts.AGE_MUL
    assert teacher.calc_life_cost() == Consts.BASE_COST["teacher"] + 4 * Consts.AGE_MUL
    assert teacher.calc_income() == Consts.BASE_INCOME["teacher"]["school"] - 4 * Consts.AGE_MUL


def test_engineer_economics():
    engineer = Engineer("Reza", 37)
    assert engineer.get_price() == int(Consts.BASE_PRICE["engineer"] * math.sqrt(Consts.MIN_AGE / 37))
    assert engineer.calc_life_cost() == int(Consts.BASE_COST["engineer"] * math.sqrt(37 / Consts.MIN_AGE))
    assert engineer.calc_income() == int(Consts.BASE_INCOME["engineer"]["company"] * math.sqrt(Consts.MIN_AGE / 37))


def test_net_balance_is_level_adjusted_income_minus_life_cost():
    company = Company("Quera")
    engineer = Engineer("Reza", 30)
    company.hire(engineer)
    engineer.level = 4
    company.level = 9

    expected = engineer.calc_income() * math.sqrt(4 * 9) - engineer.calc_life_cost()
    assert engineer.calc() == pytest.approx(expected)


def test_unemployed_person_only_pays_life_cost():
    teacher = Teacher("Niloo", 25)
    assert teacher.calc() == -teacher.calc_life_cost()


def test_upgrade_increases_level():
    worker = Worker("Amir", 18)
    worker.upgrade()
    worker.upgrade()
    assert worker.level == 3


def test_calc_all_sums_every_person():
    mine, school = Mine("Kerman"), School("Akhlagh")
    worker, teacher = Worker("Amir", 18), Teacher("Niloo", 19)
    mine.hire(worker)
    school.hire(teacher)
    unemployed = Engineer("Reza", 30)

    assert Person.calc_all() == pytest.approx(worker.calc() + teacher.calc() + unemployed.calc())
