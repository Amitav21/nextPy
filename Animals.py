class Animal:

    """
    A class used to represent an animal
    """

    """A constructor of the animal class.
    :param _name: The name of the animal.
    :param _hunger: The amount of hunger that the animal has.
    :type _name: str.
    :type _hunger: int.
    :return: None.
    :rtype: None.
    """
    def __init__(self, _name, _hunger=0):
        self._hunger = _hunger
        self._name = _name
        self.zoo_name = "Hayaton"

    """A get method for the name of the animal.
    :return: The name of the animal.
    :rtype: str.
    """
    def get_name(self):
        return self._name

    """A method for checking if the animal is hungry.
    :return: If the animal is hungry or not.
    :rtype: boolean.
    """
    def is_hungry(self):
        return self._hunger > 0

    """A method for feeding the animal (decreasing hunger level by 1).
    :return: None.
    :rtype: None.
    """
    def feed(self):
        self._hunger -= 1

    """A method for talking.
    :return: None.
    :rtype: None.
    """
    def talk(self):
        pass


class Dog(Animal):

    """
    A class used to represent a dog
    """
    def talk(self):
        print("woof woof")

    """A special method for the Dog class.
    :return: None.
    :rtype: None.
    """
    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):

    """
    A class used to represent a cat
    """
    def talk(self):
        print("meow")

    """A special method for the Cat class.
    :return: None.
    :rtype: None.
    """
    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):

    """
    A class used to represent a skunk
    """

    """A constructor of the Skunk class.
    :param _name: The name of the Skunk.
    :param _hunger: The amount of hunger that the Skunk has.
    :param _stink_count: The count of the stink the Skunk has.
    :type _name: str.
    :type _hunger: int.
    :type _stink_count: int.
    :return: None.
    :rtype: None.
    """
    def __init__(self, _name, _hunger=0, _stink_count=6):
        super().__init__(_name, _hunger)
        self._stink_count = _stink_count

    def talk(self):
        print("tsssss")

    """A special method for the Skunk class.
    :return: None.
    :rtype: None.
    """
    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):

    """
    A class used to represent a unicorn
    """
    def talk(self):
        print("Good day, darling")

    """A special method for the Unicorn class.
    :return: None.
    :rtype: None.
    """
    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):

    """
    A class used to represent a dragon
    """

    """A constructor of the Dragon class.
    :param _name: The name of the Dragon.
    :param _hunger: The amount of hunger that the Dragon has.
    :param _color: The color of the dragon.
    :type _name: str.
    :type _hunger: int.
    :type _color: str.
    :return: None.
    :rtype: None.
    """
    def __init__(self, _name, _hunger=0, _color="Green"):
        super().__init__(_name, _hunger)
        self._color = _color

    def talk(self):
        print("Raaaawr")

    """A special method for the Dragon class.
    :return: None.
    :rtype: None.
    """
    def breath_fire(self):
        print("$@#$#@$")
