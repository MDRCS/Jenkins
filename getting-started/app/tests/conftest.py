from __future__ import annotations

import pytest
from faker import Faker
from rest_framework.test import APIClient

from tests.core.survey.factories import UserFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def superuser():
    return UserFactory(is_superuser=True, is_staff=True)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def faker():
    return Faker()
