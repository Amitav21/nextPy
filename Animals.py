class Animal:

    def __init__(self, _name, _hunger = 0):
        self._hunger = _hunger
        self._name = _name
        self.zoo_name = "Hayaton"

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

    def __init__(self, _name, _hunger=0, _stink_count=6):
        super().__init__(_name, _hunger)
        self._stink_count = _stink_count
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

    def __init__(self, _name, _hunger=0, _color="Green"):
        super().__init__(_name, _hunger)
        self._color = _color
    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")




