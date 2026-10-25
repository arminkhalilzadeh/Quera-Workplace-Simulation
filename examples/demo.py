"""Build a tiny economy and print each agent's daily net balance."""

from workplace_sim import Company, Engineer, Mine, Person, School, Teacher, Worker, WorkPlace

mine, school, company = Mine("Kerman Mine"), School("Akhlagh School"), Company("Quera")
mine.upgrade()  # level 2 -> capacity 4

for name, age in [("Amir", 18), ("Sara", 22)]:
    mine.hire(Worker(name, age))
school.hire(Teacher("Niloo", 30))
company.hire(Engineer("Reza", 27))

for person in Person.instances:
    print(f"{person!r:52} net/day = {person.calc():8.1f}")
for place in WorkPlace.instances:
    print(f"{place!r:52} net/day = {place.calc():8.1f}")

print(f"\nEconomy total: {Person.calc_all() + WorkPlace.calc_all():.1f}")
