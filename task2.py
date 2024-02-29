import random

# define excludes row
excludes = []


def random_exclude(range_start: int, range_end: int):
    """
    :param range_start:
    :param range_end:
    :return:
    """
    global excludes

    # recursive errors handle
    try:
        value = random.randint(range_start, range_end)
        # check if value exists
        if value in excludes:
            # try to generate next
            return random_exclude(range_start, range_end)
        else:
            # append to row
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
    _list = []
    # iterate by range of _qty
    for _ in range(_qty):
        # append random number in range _min, _max
        res = random_exclude(_min, _max)
        if res is not None:
            _list.append(res)

    # sort ascending
    _list.sort()

    # return result
    return _list


print(get_numbers_ticket(10, 15, 5))
