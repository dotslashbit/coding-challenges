import os
lst = input().split()

def get_size_in_bytes(file):
    size = os.path.getsize(file)
    return size

def get_number_of_lines(file):
    f = open(file, 'r')
    number_of_lines = len(f.readlines())
    f.close()
    return number_of_lines

def get_number_of_words(file):
    f = open(file, 'r')
    number_of_words = 0
    for line in f:
        words = line.split()
        number_of_words += len(words)
    f.close()
    return number_of_words

def get_number_of_characters(file):
    f = open(file, 'r')
    data = f.read()
    f.close()
    number_of_characters = len(data)
    return number_of_characters

def get_all_stats(file):
    size_in_bytes = get_size_in_bytes(file)
    number_of_lines = get_number_of_lines(file)
    number_of_words = get_number_of_words(file)
    return size_in_bytes, number_of_lines, number_of_words




if lst[0] == 'ccwc':
    if len(lst) == 3:
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
        elif lst[1] == '-m':
            file = lst[2]
            number_of_characters = get_number_of_characters(file)
            print(number_of_characters)
    elif len(lst) == 2:
        file = lst[1]
        size, number_of_lines, number_of_words = get_all_stats(file)
        print(f'{number_of_lines}\t{number_of_words}\t{size}')

elif len(lst) == 5 and lst[0] == 'cat' and lst[2] == '|' and lst[3] == 'ccwc':
    file = lst[1]
    if lst[4] == '-c':
        size = get_size_in_bytes(file)
        print(size)
    elif lst[4] == '-l':
        number_of_lines = get_number_of_lines(file)
        print(number_of_lines)
    elif lst[4] == '-w':
        number_of_words = get_number_of_words(file)
        print(number_of_words)
    elif lst[4] == '-m':
        number_of_characters = get_number_of_characters(file)
        print(number_of_characters)




    
