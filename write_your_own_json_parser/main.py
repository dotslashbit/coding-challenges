# importing all the required modules
import sys

# taking the file as input
file = input()

# reading the file
try:
    f = open(file, 'r')
except FileNotFoundError:
    print('File does not exists!')
    sys.exit()

# stripping the content of the file, so that there's no extra spaces on either end of the content
lines = f.read().strip()


# dictionary to store all the key value pairs
key_value_pairs = {}

boolean_types = {'true', 'false'}
null_type = {'null'}
#print(lines)
#print(lines[0], lines[-2])

# handling if file is empty
if not lines:
    print("Empty file")

# if json file is an object, then start parsing
elif lines[0] == '{' and lines[-1] == '}':
    # print(0)

    # if the last character of the content is a ',', then its invalid
    if lines[-2] == ',':
        print('Wrong Syntax - comma found at the end')
        sys.exit()

    # list of all the attributes of the json file
    attributes = lines[1:-1].split(',')

    # iterating over each attribute
    for attribute in attributes:

        # extracting key and it's value and then stripping it
        key, value = attribute.split(':')
        key = key.strip()
        value = value.strip()
        # print(type(key))

        # if key is not string type, then its invalid
        if key[0] != '\"' or key[-1] != '\"':
            print('key is not string type')
            sys.exit()
        
        # checking value
        # checking if value is boolean
        if value in boolean_types:
            if value == "true":
                key_value_pairs[key[1:-1]] = True
            else:
                key_value_pairs[key[1:-1]] = False
        elif value in null_type:    
            key_value_pairs[key[1:-1]] = None
        elif value.isdigit():
            key_value_pairs[key[1:-1]] = int(value)
        elif value[0] == '\"' and value[-1] == '\"':
            key_value_pairs[key[1:-1]] = str(value[1:-1])
        else:
            print('Invalid Value')
            sys.exit()


        # if the key is valid, add it to the dictionary


    # printing all the key value pairs
    for k,v in key_value_pairs.items():
        print(k,v)





else:
    print(1)
