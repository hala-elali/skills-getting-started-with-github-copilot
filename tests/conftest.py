from copy import deepcopy

import pytest

from src.app import activities


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset shared in-memory activity state before and after each test."""
    original = deepcopy(activities)

    activities.clear()
    activities.update(deepcopy(original))

    yield

    activities.clear()
    activities.update(deepcopy(original))
