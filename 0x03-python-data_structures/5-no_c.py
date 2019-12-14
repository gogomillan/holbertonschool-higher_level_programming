#!/usr/bin/python3
def no_c(my_string):
    if __name__ != '__main__':
        new = ''
        new = new.join([i for i in my_string if i != 'C' and i != 'c'])
        return (new)
