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

    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    def talk(self):
        print("mewo")

    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):
   def talk(self):
     print("Good day, darling")

   def sing(self):
     print("I’m not your toy...")

class Dragon(Animal):
    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")




