import functools

def longest_name():
    with open("names.txt","r") as fp:
       print(functools.reduce(lambda x,y : x if len(x) > len(y) else y,fp.read().split('\n')))

def sum_names_length():
    with open("names.txt","r") as fp:
        print(functools.reduce(lambda x,y: x + len(y),fp.read().split('\n'),0))

def shortest_names():
    with open("names.txt","r") as fp:
        names = fp.read().split('\n')
        shortest_length = functools.reduce(lambda x,y : min(x,len(y)),names,len(names[0]))
        for name in names: print(name) if len(name) == shortest_length else None

def length_of_each_name():
    with open("name_length.txt","w") as new_fp:
        with open("names.txt","r") as fp:
            for length_of_word in map(lambda x: len(x),fp.read().split('\n')): new_fp.write(str(length_of_word) + '\n')

def names_of_specific_length():
    length = int(input("Enter the desired length: "))
    with open("names.txt","r") as fp:
        for name in list(filter(lambda x : len(x) == length,fp.read().split('\n'))): print(name)

if __name__ == '__main__':
   names_of_specific_length()
