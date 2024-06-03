import itertools

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

if __name__ == "__main__":
    for time in gen_time():
        print(time)
