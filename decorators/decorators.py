from functools import wraps


def decorator(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print("Start function")
        result = func(*args, **kwargs)
        print("Finish function")
        return result

    return inner


def id_generator(string):
    count = 0

    def inner():
        nonlocal count
        count += 1
        return f"{string}-{count:03d}"

    return inner
