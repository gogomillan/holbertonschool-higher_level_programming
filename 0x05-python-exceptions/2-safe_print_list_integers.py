#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for j in range(x):
            try:
                print("{:d}".format(my_list[j]), end='')
                i += 1
            except ValueError:
                print('', end='')
            except TypeError:
                print('', end='')
        print()
        return i
    except IndexError:
        raise
