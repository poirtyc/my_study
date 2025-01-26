from collections import defaultdict


def update_inventory(dictionary, key, value):
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value


def get_stock(dictionary, key, value=0):
    return dictionary.get(key, value)


def make_user(name_user=None, age_user=None):
    return {"name": name_user, "age": age_user}


def format_user(dicti):
    return f'{dicti["name"]}, {dicti["age"]}'


def update_dict(first_dict, second_dict):
    return first_dict.update(second_dict)


def copy_dict(dictionary):
    c = dictionary.copy()
    return c


def clear_dict(dictionary):
    dictionary.clear()


def count_all(iter_item):
    result = {}
    for item in iter_item:
        result[item] = result.get(item, 0) + 1
    return result


def collect_indexes(items):
    result = defaultdict(list)
    for index, item in enumerate(items):
        result[item].append(index)
    return result