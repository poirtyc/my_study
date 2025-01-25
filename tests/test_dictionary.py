import pytest

from dictionary.dictionary import (
    format_user,
    get_stock,
    make_user,
    update_inventory,
)


@pytest.fixture
def inventory_test():
    return {"apple": 23, "banana": 5}


@pytest.fixture
def user_dict_test():
    return {"name": "Phil", "age": 25}


def test_update_inventory(inventory_test):
    update_inventory(inventory_test, "coffee", 10)
    assert inventory_test == {"apple": 23, "banana": 5, "coffee": 10}

    update_inventory(inventory_test, "coffee", 10)
    assert inventory_test == {"apple": 23, "banana": 5, "coffee": 20}


def test_get_stock(inventory_test):
    assert get_stock(inventory_test, "apple") == 23
    assert get_stock(inventory_test, "monkey") == 0


def test_make_user(user_dict_test):
    phill = make_user("Phil", 25)
    assert phill == user_dict_test

    john = make_user()
    assert john == {"age": None, "name": None}


def test_format_user(user_dict_test):
    assert format_user(user_dict_test) == "Phil, 25"
