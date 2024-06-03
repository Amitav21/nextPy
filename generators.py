import itertools
import time


def gen_secs():
    for i in range (60):
        yield i

def gen_minutes():
    for i in range (60):
        yield i

def gen_hours():
    for i in range (24):
        yield i

def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02}:{minute:02}:{second:02}"

def gen_years(start=2019):
    while start <= time.gmtime().tm_year:
        yield start
        start += 1

def gen_months():
    for i in range (1,13):
        yield i

def gen_days(month, leap_year=True):
    month_to_days = {1:31, 2:28, 2.5:29, 3:31, 4:30, 5:31, 6:30,
        7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if leap_year and month == 2:
        month = 2.5
    for day in range(1, month_to_days[month] + 1):
        yield day

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
