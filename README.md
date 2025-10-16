
# Quera Country Simulator — OOP Mini Project

A compact economic–social simulator designed to showcase **Object-Oriented Programming** in Python.
It implements a clean model of **people** (`Engineer`, `Teacher`, `Worker`) and **workplaces**
(`Mine`, `School`, `Company`) built on top of the base classes `Person` and `WorkPlace`.

> This repository is structured to be **portfolio-ready**: clear package layout, unit tests (pytest),
and CI (GitHub Actions).

## ✨ Highlights
- **Clean OOP hierarchy**: `Person` and `WorkPlace` with job- and workplace-specific subclasses.
- **Hiring & capacity rules** with bidirectional links (`person.work_place` ↔ `workplace.employees`).
- **Daily net calculation**: income adjusted by levels (person/workplace), life cost, and workplace maintenance.
- **Unit tests** with `pytest` and ready-to-use **CI** workflow.
- **Readable code** with type hints and simple constants-based configuration (`Consts`).

## 📦 Project Structure
```
country/
  models/
    person.py
    employees/
      engineer.py
      teacher.py
      worker.py
    workplaces/
      work_place.py
      mine.py
      school.py
      company.py
tests/
  test_hiring.py
  test_income.py
requirements.txt
README.md
```

## 🚀 Quickstart
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
pytest -q
```

## 🧪 What the tests cover
- **Hiring & capacity**: attempts to hire beyond capacity raise `WorkPlaceIsFull`.
- **Income & net**: income is job+workplace-dependent; net = adjusted income − life cost.
- **Workplace economics**: daily maintenance costs contribute negative net for workplaces.

## 🧩 Core Design
- **Income adjustment** (in `Person.do_level`):  
  `adjusted_income = base_income * sqrt(person.level * workplace.level)`
- **Workplace capacity & costs**:  
  - `Mine`: `capacity = level^2`, `costs = BASE_PLACE_COST + LEVEL_MUL * level`  
  - `School`: `capacity = floor(sqrt(level))`, `costs = BASE_PLACE_COST * floor(sqrt(level))`  
  - `Company`: `capacity = level`, `costs = BASE_PLACE_COST * level`

All economic constants live in `Consts` for clarity and easy tweaking.

## 🧭 Example
```python
from country.models.workplaces.mine import Mine
from country.models.employees.engineer import Engineer

m = Mine("M1")              # capacity computed for level=1
e = Engineer("Ali", 25)
m.hire(e)

print("Base income:", e.calc_income())
print("Net (daily):", e.calc())     # adjusted by levels minus life cost
print("Workplace net:", m.calc())   # negative maintenance cost
```

## 🔧 Tooling
- **Python**: 3.10+
- **Tests**: `pytest`
- **CI**: GitHub Actions workflow in `.github/workflows/ci.yml`
- **Code style**: Type hints, straightforward modules (you can add ruff/black later if desired)

## 🗺️ Roadmap
- CLI/Streamlit mini-dashboard for running scenarios
- Hiring policies (FCFS / merit-based / lottery)
- Random shocks (strikes, breakdowns) and basic tax/inflation knobs
- Docs: `docs/model.md`, UML diagram, charts for simulation runs

## 📄 License
MIT — see [LICENSE](./LICENSE).

---

If you find this useful, feel free to star the repo ⭐ and open issues for ideas or improvements!
