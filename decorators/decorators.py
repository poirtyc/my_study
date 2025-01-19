def decorator(func):

    def inner(*args, **kwargs):
        print("Start function")
        result = func(*args, **kwargs)
        print("Finish function")
        return result

    return inner