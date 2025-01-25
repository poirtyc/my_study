def update_inventory(dictionary, key, value):
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value


def get_stock(dictionary, key, value=0):
    return dictionary.get(key, value)
