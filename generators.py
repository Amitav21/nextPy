def gen_secs():
    for i in range (59):
        yield i


if __name__ == "__main__":
    for second in gen_secs():
        print(second)
