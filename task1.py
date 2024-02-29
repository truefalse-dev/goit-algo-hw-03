from datetime import datetime


def get_days_from_today(date_str: str):
    """
    :param date_str:
    :return:
    """
    try:
        # build datetime object based on string format %Y-%m-%d
        date_input = datetime.strptime(date_str, '%Y-%m-%d').date()

        # get datetime object from today
        date_today = datetime.today().date()

        # calculate difference
        diff = date_today - date_input

        # return difference in days integer
        return diff.days

    # catch ValueError exception if input format failed
    except ValueError as error:
        # return formatted error line
        return f"Invalid input {error}"


# execute function and print result
print(get_days_from_today('1982-11-21'))
