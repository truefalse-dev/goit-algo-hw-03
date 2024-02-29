from datetime import datetime, timedelta


def next_monday(_datetime: datetime) -> datetime:
    """
    :param _datetime:
    :return:
    """
    days_ahead = 0 - _datetime.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return _datetime + timedelta(days_ahead)


def get_upcoming_birthdays(_users: list) -> list:
    """
    :param _users:
    """
    # get today datetime object
    date_today = datetime.today().date()

    # define start of the week relatively today
    start = date_today - timedelta(days=date_today.weekday())

    # define row of weekdays from start
    weekdays = [start + timedelta(days=x) for x in range(0, 7)]

    # define empty list
    _list = []

    # go over _users row
    for user in _users:
        # try to get a birthday with replace of year to current
        try:
            date_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=datetime.now().year)

        # then except do pass
        except ValueError:
            continue

        # conditions then birthday upcoming and will be in current week
        if date_birthday > date_today and date_birthday in weekdays:

            # move greeting to next monday if birthday in this weekend
            if date_birthday.weekday() in (5, 6):
                date_birthday = next_monday(date_birthday)

            # fill the result list
            _list.append({
                'user': user['name'],
                'congratulation_date': date_birthday.strftime("%d.%m.%Y")
            })

    # return result list
    return _list


users = [
    {"name": "John Doe", "birthday": "1985.02.27"},
    {"name": "Jane Smith", "birthday": "1990.03.02"},
    {"name": "Maria", "birthday": "1982.02.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(f"Список привітань на цьому тижні: {upcoming_birthdays}")
