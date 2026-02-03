import copy
import pytest
from fastapi.testclient import TestClient

from src import app as app_module

@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activities dict after each test to keep tests isolated."""
    original = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(original)


@pytest.fixture
def client():
    from src.app import app

    return TestClient(app)
