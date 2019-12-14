#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if __name__ != '__main__':
        a = my_list
        a.reverse()
        [print("{:d}".format(i)) for i in a]
