import pytest
from closure.ordered_count import say_hello_with_name, summator, counter


@pytest.fixture
def say_hello_with_name_func():
    return say_hello_with_name


@pytest.fixture
def summator_func():
    return summator


@pytest.fixture
def counter_func():
    return counter


def test_closing(say_hello_with_name_func):
    greeting_func = say_hello_with_name_func("Vasya")
    assert greeting_func() == "Hello, Vasya"


def test_summator(summator_func):
    greeting_func = summator_func(10)
    assert greeting_func(2) == 12
    assert greeting_func(5) == 15


def test_counter(counter_func):
    greeting_func = counter_func()
    assert greeting_func() == 1
    assert greeting_func() == 2
    assert greeting_func() == 3
