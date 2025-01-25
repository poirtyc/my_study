import pytest

from dictionary.dictionary import get_stock, update_inventory


@pytest.fixture
def dictionary_for_test():
    return {"apple": 23, "banana": 5}


def test_update_inventory(dictionary_for_test):
    update_inventory(dictionary_for_test, "coffee", 10)
    assert dictionary_for_test == {"apple": 23, "banana": 5, "coffee": 10}

    update_inventory(dictionary_for_test, "coffee", 10)
    assert dictionary_for_test == {"apple": 23, "banana": 5, "coffee": 20}


def test_get_stock(dictionary_for_test):
    assert get_stock(dictionary_for_test, "apple") == 23
    assert get_stock(dictionary_for_test, "monkey") == 0
