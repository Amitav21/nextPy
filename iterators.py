
"""Checks if a given id is valid.
    :param id_number: the given id.
    :type id_number: int.
    :return: True if the id is valid, otherwise False.
    :rtype: bool.
    """
def check_id_valid(id_number):
    sum = 0
    even_flag = False
    # double each digit
    double_iter = map(lambda x: int(x) * 2, str(id_number))
    for num in double_iter:
        # if the index is odd, return it to the base value
        if even_flag == False:
            num = num/2
        # if its even, it means it was doubled by 2 and we need to check it
        else:
            if num > 9:
                num = num % 10 + num // 10
        even_flag = not even_flag
        sum += num
    if sum % 10 != 0:
        return False
    return True



class IDIterator:

    """
    A class used to represent an Id iterator
    """

    """A constructor of the IDIterator class.
        :param _id: The given id.
        :type _id: int.
        :return: None.
        :rtype: None.
    """
    def __init__(self, _id):
        self._id = _id

    """A method for returning the iterator instance.
        :return: An IDIterator object .
        :rtype: IDIterator.
        """
    def __iter__(self):
        return self

    """A method for iterating the current IDIterator instance.
        :return: the next valid id.
        :rtype: int.
        :raise: StopIteration: raises an Exception
        """
    def __next__(self):
        self._id += 1
        while not check_id_valid(self._id):
            self._id += 1
            if self._id == 999999999:
                raise StopIteration
        return self._id

"""A method for generating valid id's.
    :param id: The given id.
    :type id: int.
    :return: the next generated id.
    :rtype: int.
    """
def id_generator(id):
        while id < 999999999:
            id += 1
            while not check_id_valid(id):
                id += 1
            yield id


if __name__ == "__main__":
    id = int(input("enter the id: "))
    choice = input("Generator or Iterator? (gen/it)?: ")
    if choice == "gen":
        id_gen = id_generator(id)
        for i in range(10):
            print(next(id_gen))
    elif choice == "it":
        id_iter = IDIterator(id)
        for i in range(10):
            print(id_iter.__next__())
