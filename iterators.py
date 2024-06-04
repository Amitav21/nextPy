
def check_id_valid(id_number):
    sum = 0
    even_flag = False
    double_iter = map(lambda x: int(x) * 2, str(id_number))
    for num in square_iter:
        if even_flag == False:
            num = num/2
        else:
            if num > 9:
                num = num % 10 + num // 10
        even_flag = not even_flag
        sum += num
    if sum % 10 != 0:
        return False
    return True



class IDIterator:

    def __init__(self, _id):
        self._id = _id

    def __iter__(self):
        return self

    def __next__(self):
        while not check_id_valid(self._id):
            self._id += 1
            if self._id == 999999999:
                raise StopIteration
        return self._id


if __name__ == "__main__":
    print(check_id_valid(123456780))
    print(check_id_valid(123456782))