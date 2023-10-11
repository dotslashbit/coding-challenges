# TODO --> Modify the attributes breakdown , otherwise it can't handle nested objects and values and that's why its throwing error

# importing all the required modules
import sys

# taking the file as input
def input_processing():
    file = input()

    # reading the file
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        print('File does not exists!')
        sys.exit()

    # stripping the content of the file, so that there's no extra spaces on either end of the content
    lines = f.read().strip()
    return lines

def validate_JSON_object(lines):

    if not lines:
        print("Empty file")
        return False


    # if json file is an object, then start parsing
    elif lines[0] == '{' and lines[-1] == '}':
        # print(0)

        # if the last character of the content is a ',', then its invalid
        if lines[-2] == ',':
            print('Wrong Syntax - comma found at the end')
            return False
    else:
        print("Not a valid JSON file")
        return False
    return True



def validate_key(lines):
    attributes = lines[1:-1].split(',',1)
    print(attributes)
    # iterating over each attribute
    for attribute in attributes:
        print(attribute)

        # extracting key and it's value and then stripping it
        key, value = attribute.split(':')
        key = key.strip()
        value = value.strip()
        # print(type(key))

        # if key is not string type, then its invalid
        if key[0] != '\"' or key[-1] != '\"':
            print('key is not string type')
            return False
    return True

def validate_value(lines):
    # checking value
    # checking if value is boolean
    attributes = lines[1:-1].split(',',1)

    # iterating over each attribute
    for attribute in attributes:

        # extracting key and it's value and then stripping it
        key, value = attribute.split(':')
        value = value.strip()
        print(value)
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
        elif value[0] == '{' and value[-1] == '}':
            #validate_JSON_file = validate_JSON_object(value)
            #if not validate_JSON_file:
            #    sys.exit()

            key_value_pairs[key[1:-1]] = value
        elif value[0] == '[' and value[-1] == ']':
            key_value_pairs[key[1:-1]] = value
        else:
            print('Invalid Value')
            return False
    return True



lines = input_processing()


# dictionary to store all the key value pairs
key_value_pairs = {}

boolean_types = {'true', 'false'}
null_type = {'null'}
#print(lines)
#print(lines[0], lines[-2])

# handling if file is empty

validate_JSON_file = validate_JSON_object(lines)
if not validate_JSON_file:
    sys.exit()

validate_keys = validate_key(lines)
if not validate_keys:
    sys.exit()

validate_values = validate_value(lines)
if not validate_values:
    sys.exit()


# if the key is valid, add it to the dictionary


# printing all the key value pairs
#for k,v in key_value_pairs.items():
#    print(k,v)






