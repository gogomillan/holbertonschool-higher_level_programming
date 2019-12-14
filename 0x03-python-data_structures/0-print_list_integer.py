#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if __name__ != '__main__':
        [print("{:d}".format(i)) for i in my_list]
