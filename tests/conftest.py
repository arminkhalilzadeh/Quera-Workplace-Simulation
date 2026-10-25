import pytest

from workplace_sim import Person, WorkPlace


@pytest.fixture(autouse=True)
def _reset_registries():
    """Each test starts with empty Person/WorkPlace registries."""
    Person.instances.clear()
    WorkPlace.instances.clear()
    yield
    Person.instances.clear()
    WorkPlace.instances.clear()
