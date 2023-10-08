file = input()
f = open(file, 'r')
lines = f.read()
if not lines:
    print(1)
elif lines[0] == '{' and lines[-1] == '}':
    print(0)
else:
    print(1)
