import pytest

from closure.closure import (
    average_numbers,
    counter,
    func_call_counter,
    say_hello_with_name,
    summator,
)


@pytest.fixture
def say_hello_with_name_func():
    return say_hello_with_name


@pytest.fixture
def summator_func():
    return summator


@pytest.fixture
def counter_func():
    return counter


@pytest.fixture
def average_numbers_func():
    return average_numbers


@pytest.fixture
def func_call_counter_test():
    return func_call_counter


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


def test_average_numbers(average_numbers_func):
    greeting_func = average_numbers_func()
    assert greeting_func(5) == 5
    assert greeting_func(10) == 7.5
    assert greeting_func(15) == 10


def test_func_call_counter(capsys, func_call_counter_test):
    def add(a, b):
        return a + b

    test_add = func_call_counter_test(add)

    assert test_add(2, 3) == 5
    captured = capsys.readouterr()
    assert captured.out.strip() == "add function was calling 1 times"

    assert test_add(4, 6) == 10
    captured = capsys.readouterr()
    assert captured.out.strip() == "add function was calling 2 times"
