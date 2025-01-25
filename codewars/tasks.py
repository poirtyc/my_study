from math import ceil


def vowel_indices(word):
    return [k + 1 for k, v in enumerate(word.lower()) if v in "aeiouy"]


def high_and_low(numbers):
    arr = [int(s) for s in numbers.split(" ")]
    return f"{max(arr)} {min(arr)}"


def to_float_array(arr):
    return [float(item) for item in arr]


def max_diff(lst):
    if not lst:
        return 0
    return abs(max(lst) - min(lst))


def div_con(x):
    if not x:
        return 0
    sum_non_string = sum(i for i in x if isinstance(i, int))
    sum_string = sum(int(i) for i in x if isinstance(i, str))
    return sum_non_string - sum_string


def sort_gift_code(code):
    return "".join(sorted(code))


def cooking_time(eggs):
    if not eggs:
        return 0
    return ceil(eggs / 8) * 5


def sum_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))
