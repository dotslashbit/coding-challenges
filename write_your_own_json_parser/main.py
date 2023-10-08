# importing all the required modules
import sys

# taking the file as input
file = input()

# reading the file
f = open(file, 'r')

# stripping the content of the file, so that there's no extra spaces on either end of the content
lines = f.read().strip()


# dictionary to store all the key value pairs
key_value_pairs = {}
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
        # print(key)

        # if key is not string type, then its invalid
        if key[0] != '\"' or key[-1] != '\"':
            print('key is not string type')
            sys.exit()
        
        # if the key is valid, add it to the dictionary
        key_value_pairs[key[1:-1]] = value[1:-1]

    # printing all the key value pairs
    for k,v in key_value_pairs.items():
        print(k,v)





else:
    print(1)
