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
