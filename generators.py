def gen_secs():
    for i in range (59):
        yield i

def gen_minutes():
    for i in range (59):
        yield i


if __name__ == "__main__":
    for second in gen_secs():
        print(second)
    for minute in gen_minutes():
        print(minute)
