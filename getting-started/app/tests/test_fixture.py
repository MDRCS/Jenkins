import pytest


@pytest.mark.django_db
def test_user_fixture(user):
    assert user.id
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_superuser_fixture(superuser):
    assert superuser.id
    assert superuser.is_staff
    assert superuser.is_superuser
