#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            upc = ord(x) - 32
        else:
            upc = ord(x)
        print("{:c}".format(upc), end='')
    print("")
