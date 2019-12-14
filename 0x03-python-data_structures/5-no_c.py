#!/usr/bin/python3
def no_c(my_string):
    if __name__ != '__main__':
        new = ''
        if my_string is None:
            return (new)
        new = new.join([i for i in my_string if i != 'C' or i != 'c'])
        return (new)
