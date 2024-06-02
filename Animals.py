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

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

class Cat(Animal):
    def talk(self):
        print("mewo")

class Skunk(Animal):
    def talk(self):
        print("tsssss")

class Unicorn(Animal):
   def talk(self):
        print("Good day, darling")

class Dragon(Animal):
    def talk(self):
        print("Raaaawr")




