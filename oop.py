from Animals import Animal,Dog,Cat,Skunk,Unicorn,Dragon

def main():
    dog = Dog("Brownie",10)
    cat = Cat("Zelda",3)
    skunk = Skunk("Stinky",0)
    unicorn = Unicorn("Keith",7)
    dragon = Dragon("Lizzy",1450)
    zoo_lst = [dog,cat,skunk,unicorn,dragon]
    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.__class__.__name__,animal.get_name())
            while animal.is_hungry():
                animal.feed()
            animal.talk()


if __name__ == '__main__':
   main()
