#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
            except ValueError:
                print('', end='')
        print()
        if i > 0:
            return i + 1
        else:
            return i
    except IndexError:
        raise
