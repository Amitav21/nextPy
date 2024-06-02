class Animal:

    def __init__(self, _name, _hunger = 0):
        self._hunger = _hunger
        self._name = _name

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1


class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Skunk(Animal):
    pass

class Unicorn(Animal):
    pass

class Dragon(Animal):
    pass




