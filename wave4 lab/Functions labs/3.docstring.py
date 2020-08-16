def readable_timedelta(days):
    # insert your docstring here
    '''Calculate the number of days(readable_timedelta) and weeks in a given integer arguement
    INPUT:
    days: int. The argument passed in number of days
    '''

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)