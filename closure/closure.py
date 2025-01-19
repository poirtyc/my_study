def say_hello_with_name(name):
    def inner():
        return f"Hello, {name}"

    return inner


def summator(a):
    def inner(b):
        return a + b

    return inner


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


def average_numbers():
    summa = 0
    count = 0

    def inner(num):
        nonlocal summa
        nonlocal count
        summa += num
        count += 1
        return summa / count

    return inner


def func_call_counter(func):
    count = 1

    def inner(*args, **kwargs):
        nonlocal count
        print(f"{func.__name__} function was calling {count} times")
        result = func(*args, **kwargs)
        count += 1
        return result

    return inner
