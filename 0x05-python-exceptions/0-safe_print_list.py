#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
        print()
        if i > 0:
            return i + 1
        else:
            return i
    except:
        print()
        return i
