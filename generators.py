def gen_secs():
    for i in range (60):
        yield i

def gen_minutes():
    for i in range (60):
        yield i

def gen_hours():
    for i in range (24):
        yield i


if __name__ == "__main__":
    for second in gen_secs():
        print(second)
    for minute in gen_minutes():
        print(minute)
    for hour in gen_hours():
        print(hour)
