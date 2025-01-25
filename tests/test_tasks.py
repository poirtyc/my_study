from codewars.tasks import (
    cooking_time,
    div_con,
    high_and_low,
    max_diff,
    sort_gift_code,
    sum_cubes,
    to_float_array,
    vowel_indices,
)


def test_vowel():
    assert vowel_indices("Apple") == [1, 5]
    assert vowel_indices("Super") == [2, 4]


def test_high_and_low():
    assert high_and_low("1 2 3 4 5") == "5 1"
    assert high_and_low("1 2 -3 4 5") == "5 -3"
    assert high_and_low("1 9 3 4 -5") == "9 -5"
    assert high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9"


def test_to_float_array():
    assert to_float_array(["1.1", "2.2", "3.3"]) == [1.1, 2.2, 3.3]


def test_max_diff():
    assert max_diff([]) == 0
    assert max_diff([1, 2, 3, 4]) == 3
    assert max_diff([0, 1, 2, 3, 4, 5, 6]) == 6
    assert max_diff([-0, 1, 2, -3, 4, 5, -6]) == 11


def test_div_con():
    assert div_con([]) == 0
    assert div_con([9, 3, "7", "3"]) == 2
    assert div_con(["1", "5", "8", 8, 9, 9, 2, "3"]) == 11
    assert div_con(["5", "0", 9, 3, 2, 1, "9", 6, 7]) == 14


def test_sort_gift_code():
    assert sort_gift_code("abcdef") == "abcdef"
    assert sort_gift_code("zyxwvutsrqponmlkjihgfedcba") == \
    "abcdefghijklmnopqrstuvwxyz"


def test_cooking_time():
    assert cooking_time(10) == 10
    assert cooking_time(17) == 15
    assert cooking_time(0) == 0


def test_cum_cubes():
    assert sum_cubes(3) == 36
    assert sum_cubes(1) == 1
    assert sum_cubes(2) == 9
