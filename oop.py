from Animals import Animal,Dog,Cat,Skunk,Unicorn,Dragon

def main():
    dog = Dog("Brownie",10)
    cat = Cat("Zelda",3)
    skunk = Skunk("Stinky",0)
    unicorn = Unicorn("Keith",7)
    dragon = Dragon("Lizzy",1450)
    dog2 = Dog("Doggo",80)
    cat2 = Cat("Kitty",80)
    skunk2 = Skunk("Stinky Jr.",80)
    unicorn2 = Unicorn("Clair",80)
    dragon2 = Dragon("McFly",80)
    zoo_lst = [dog,cat,skunk,unicorn,dragon,dog2,cat2,skunk2,unicorn2,dragon2]
    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.__class__.__name__,animal.get_name())
            while animal.is_hungry():
                animal.feed()
            animal.talk()

            # activating each animal's special method according to it's class
            if isinstance(animal, Dog):
                animal.fetch_stick()
            elif isinstance(animal, Cat):
                animal.chase_laser()
            elif isinstance(animal, Skunk):
                animal.stink()
            elif isinstance(animal, Unicorn):
                animal.sing()
            elif isinstance(animal, Dragon):
                animal.breath_fire()
    print(zoo_lst[0].zoo_name)


if __name__ == '__main__':
   main()
