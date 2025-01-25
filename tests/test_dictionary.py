
import pytest

from dictionary.dictionary import (
    clear_dict,
    copy_dict,
    count_all,
    format_user,
    get_stock,
    make_user,
    update_dict,
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


def test_update_dict():
    cart = {"apples": 2, "oranges": 1}
    addon = {"oranges": 5, "lemons": 3}
    update_dict(cart, addon)
    assert cart == {"apples": 2, "oranges": 5, "lemons": 3}


def test_copy_dict(inventory_test):
    d = copy_dict(inventory_test)
    assert id(d) != id(inventory_test)


def test_clear_dict(inventory_test):
    clear_dict(inventory_test)
    assert inventory_test == {}


def test_count_all():
    assert count_all(["cat", "dog", "cat"]) == {"cat": 2, "dog": 1}
    assert count_all("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
