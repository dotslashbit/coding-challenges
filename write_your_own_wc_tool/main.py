import os
lst = input().split()

def get_size_in_bytes(file):
    size = os.path.getsize(file)
    return size

def get_number_of_lines(file):
    f = open(file, 'r')
    number_of_lines = len(f.readlines())
    return number_of_lines

def get_number_of_words(file):
    f = open(file, 'r')
    number_of_words = 0
    for line in f:
        words = line.split()
        number_of_words += len(words)
    return number_of_words



if lst[0] == 'cwcc':
    if lst[1] == '-c':
        file = lst[2]
        size = get_size_in_bytes(file)
        print(size)
    elif lst[1] == '-l':
        file = lst[2]
        number_of_lines = get_number_of_lines(file)
        print(number_of_lines)
    elif lst[1] == '-w':
        file = lst[2]
        number_of_words = get_number_of_words(file)
        print(number_of_words)
    
