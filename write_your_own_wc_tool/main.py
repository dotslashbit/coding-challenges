import os
lst = input().split()

def get_size_in_bytes(file):
    size = os.path.getsize(file)
    return size


if lst[0] == 'cwcc':
    if lst[1] == '-c':
        file = lst[2]
        size = get_size_in_bytes(file)
        print(size)

