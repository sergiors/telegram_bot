import calendar
from datetime import date, timedelta


def next_month(dt: date) -> date:
    _, ndays = calendar.monthrange(dt.year, dt.month)
    return dt + timedelta(days=ndays)
