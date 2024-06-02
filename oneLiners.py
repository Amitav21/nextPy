import functools

"""Opens a file of names and prints the longest name in the file.
    """
def longest_name():
    with open("names.txt","r") as fp:
       print(functools.reduce(lambda x,y : x if len(x) > len(y) else y,fp.read().split('\n')))

"""Opens a file of names and prints the sum of the names' lengths.
    """
def sum_names_length():
    with open("names.txt","r") as fp:
        print(functools.reduce(lambda x,y: x + len(y),fp.read().split('\n'),0))

"""Opens a file of names and prints the shortest names in the file.
    """
def shortest_names():
    with open("names.txt","r") as fp:
        names = fp.read().split('\n')
        shortest_length = functools.reduce(lambda x,y : min(x,len(y)),names,len(names[0]))
        for name in names: print(name) if len(name) == shortest_length else None


"""Opens a file of names and creates a new file with the names' lengths.
    """
def length_of_each_name():
    with open("name_length.txt","w") as new_fp:
        with open("names.txt","r") as fp:
            for length_of_word in map(lambda x: len(x),fp.read().split('\n')): new_fp.write(str(length_of_word) + '\n')

"""Opens a file of names, reads a specific length and prints the names with the same length as entered.
    """
def names_of_specific_length():
    length = int(input("Enter the desired length: "))
    with open("names.txt","r") as fp:
        for name in list(filter(lambda x : len(x) == length,fp.read().split('\n'))): print(name)

if __name__ == '__main__':
   names_of_specific_length()
