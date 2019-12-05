#!/usr/bin/python3
sep = ""
for x in range(0, 9):
    for y in range(x + 1, 10):
        if (x + y) != 1:
            sep = ", "
        print("{}{:d}{:d}".format(sep, x, y), end='')
print('')
