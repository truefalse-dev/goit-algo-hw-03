import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(num: str) -> str:
    """
    :param num:
    :return:
    """
    # get only numbers [0-9]
    string_re = re.sub("\\D", "", num)

    # cut off 10 symbols at end
    phone_without_code = string_re[len(string_re) - 10:]

    # append prefix +38
    return f'+38{phone_without_code}'


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
