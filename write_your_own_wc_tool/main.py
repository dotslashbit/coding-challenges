import os

# taking input
lst = input().split()

# function to get the size of file in bytes
def get_size_in_bytes(file):
    size = os.path.getsize(file)
    return size

# function to get the total number of lines
def get_number_of_lines(file):
    f = open(file, 'r')
    number_of_lines = len(f.readlines())
    f.close()
    return number_of_lines

# function to get the total number of words
def get_number_of_words(file):
    f = open(file, 'r')
    number_of_words = 0
    for line in f:
        words = line.split()
        number_of_words += len(words)
    f.close()
    return number_of_words

# function to get the total number of characters
def get_number_of_characters(file):
    f = open(file, 'r')
    data = f.read()
    f.close()
    number_of_characters = len(data)
    return number_of_characters

# function to get all the statistics about the file
def get_all_stats(file):
    size_in_bytes = get_size_in_bytes(file)
    number_of_lines = get_number_of_lines(file)
    number_of_words = get_number_of_words(file)
    return size_in_bytes, number_of_lines, number_of_words



# checking if the first input is the `ccwc` command or not
if lst[0] == 'ccwc':
    # checking the length of the input, just to know if input is valid or not using length
    if len(lst) == 3:

        # storing the file name
        file = lst[2]
        # handling all the different operations
        if lst[1] == '-c':
            size = get_size_in_bytes(file)
            print(size)
        elif lst[1] == '-l':
            number_of_lines = get_number_of_lines(file)
            print(number_of_lines)
        elif lst[1] == '-w':
            number_of_words = get_number_of_words(file)
            print(number_of_words)
        elif lst[1] == '-m':
            number_of_characters = get_number_of_characters(file)
            print(number_of_characters)
    # codition for the case, where operation is not mentioned
    elif len(lst) == 2:
        file = lst[1]
        size, number_of_lines, number_of_words = get_all_stats(file)
        print(f'{number_of_lines}\t{number_of_words}\t{size}')

# condition when file is not passed in the `ccwc` command
elif len(lst) == 5 and lst[0] == 'cat' and lst[2] == '|' and lst[3] == 'ccwc':
    # storing the file name
    file = lst[1]

    # handling all the different operations
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




    
