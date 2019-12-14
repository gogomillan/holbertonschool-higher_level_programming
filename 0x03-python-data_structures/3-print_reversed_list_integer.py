#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if __name__ != '__main__':
        if my_list is None:
            return
        tmp = my_list.copy()
        tmp.reverse()
        [print("{:d}".format(i)) for i in tmp]
