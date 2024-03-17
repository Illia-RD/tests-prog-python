# 9. TODO Напишіть програму, яка визначає, чи є введений рік високосним.


def input_data():
    year_input = int(input("введіть рік \n"))
    return year_input


# на чистому пітоні
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return f"{year} не високосний"

        return f"{year} рік високосний"
    else:
        return f"{year} рік не високосний"


# модуль datatime
"""
from datetime import datetime


def is_leap_year(year):
    try:
        datetime(year, 2, 29)
        return f"{year} рік високосний"
    except ValueError:
        return f"{year} рік не високосний"

"""


# вбудована функція calendar
"""
import calendar

def is_leap_year(year):

    return (
        f"{year} рік високосний"
        if calendar.isleap(year) == True
        else f"{year} рік не високосний"
    )
"""

print(is_leap_year(input_data()))
