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


def copy_dict(dict):
    c = dict.copy()
    return c


def clear_dict(dict):
    dict.clear()


def count_all(iter_item):
    dict = {}
    for item in iter_item:
        if item not in dict.keys():
            dict[item] = 1
        else:
            dict[item] += 1
    return dict
