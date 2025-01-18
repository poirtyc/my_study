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
