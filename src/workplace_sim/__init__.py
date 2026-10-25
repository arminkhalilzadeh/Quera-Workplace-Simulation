"""An object-oriented simulation of people, jobs and workplaces."""

from workplace_sim.people import Engineer, Person, Teacher, Worker
from workplace_sim.workplaces import Company, Mine, School, WorkPlace, WorkPlaceIsFull

__all__ = [
    "Company",
    "Engineer",
    "Mine",
    "Person",
    "School",
    "Teacher",
    "WorkPlace",
    "WorkPlaceIsFull",
    "Worker",
]
