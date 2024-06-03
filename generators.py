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
        start = start + 1

def gen_months():
    for i in range (1,13):
        yield i

if __name__ == "__main__":
    for month in gen_months():
        print(month)
