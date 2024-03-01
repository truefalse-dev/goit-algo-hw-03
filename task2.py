import random


# define excludes row

def random_exclude(range_start: int, range_end: int, excludes):
    """
    :param range_start:
    :param range_end:
    :param excludes:
    :return:
    """
    # recursive errors handle
    try:
        value = random.randint(range_start, range_end)
        # check if value exists
        if value in excludes:
            # try to generate next
            return random_exclude(range_start, range_end, excludes)
        else:
            # append to excludes row
            excludes.append(value)

    # set value = 0 if reaching recursive depth
    except RecursionError:
        value = None

    return value


def get_numbers_ticket(_min: int, _max: int, _qty: int) -> list:
    """
    :param _min:
    :param _max:
    :param _qty:
    :return:
    """
    _excludes, _list = [], []

    # check input values
    if not validated(_min, _max, _qty):
        return _list

    # iterate by range of _qty
    for _ in range(_qty):
        # append random number in range _min, _max
        res = random_exclude(_min, _max, _excludes)
        if res is not None:
            _list.append(res)

    # sort ascending
    _list.sort()

    # return result
    return _list


def validated(_min: int, _max: int, _qty: int) -> bool:
    """
    :param _min:
    :param _max:
    :param _qty:
    """
    if _qty < 1:
        print("Invalid :quantity (> 0)")
        return False

    if _min >= _max or _min < 1 or _max > 1000:
        print("Invalid :min (> 0) or :max (<=1000)")
        return False

    return True


print(get_numbers_ticket(10, 5, -2))  # input error
print(get_numbers_ticket(0, 400, 17))  # input error
print(get_numbers_ticket(10, 14, 6))
print(get_numbers_ticket(10, 15, 5))
