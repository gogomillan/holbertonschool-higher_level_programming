#!/usr/bin/python3
sep = ", "
for x in range(0, 100):
    if x == 99:
        sep = ""
    print("{:02d}{}".format(x, sep), end='')
print('')
