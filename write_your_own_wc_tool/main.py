import os
lst = input().split()
if lst[0] == 'cwcc':
    if lst[1] == '-c':
        file = lst[2]
        print(file)
        f = open(file, 'r')
        #content = f.read()
        #size = len(content)
        #print(size)

