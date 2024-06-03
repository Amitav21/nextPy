import itertools
import time

"""A method for generating the range of seconds.
:return: the current second.
:rtype: Generator.
"""
def gen_secs():
    for i in range (60):
        yield i

"""A method for generating the range of minutes.
:return: the current minute.
:rtype: Generator.
"""
def gen_minutes():
    for i in range (60):
        yield i

"""A method for generating the range of hours.
:return: the current hour.
:rtype: Generator.
"""
def gen_hours():
    for i in range (24):
        yield i

"""A method for generating the range of times.
:return: the current time.
:rtype: Generator.
"""
def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02}:{minute:02}:{second:02}"

"""A method for generating the range of years from the given year until now.
:return: the current year.
:rtype: Generator.
"""
def gen_years(start=2019):
    while start <= time.gmtime().tm_year:
        yield start
        start += 1

"""A method for generating the range of months.
:return: the current month.
:rtype: Generator.
"""
def gen_months():
    for i in range (1,13):
        yield i

"""A method for generating the range of days in a given month according if its a leap year.
:return: the current day.
:rtype: Generator.
"""
def gen_days(month, leap_year=True):
    month_to_days = {1:31, 2:28, 2.5:29, 3:31, 4:30, 5:31, 6:30,
        7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if leap_year and month == 2:
        month = 2.5
    for day in range(1, month_to_days[month] + 1):
        yield day

"""A method for generating the range of dates from 01/01/2019.
:return: the current date.
:rtype: Generator.
"""
def gen_date():
    for year in gen_years():
        if year % 4 == 0:
            for month in gen_months():
                for day in gen_days(month):
                    for time in gen_time():
                        yield (f"{day}/{month}/{year}" + time)
        else:
            for month in gen_months():
                for day in gen_days(month,False):
                    for time in gen_time():
                        yield (f"{day}/{month}/{year} " + time)

if __name__ == "__main__":
    counter = -1
    for date in gen_date():
        counter += 1
        if counter % 1000000 == 0 and counter != 0:
            print(date)
