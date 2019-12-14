#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if __name__ != '__main__':
        tmp = my_list.copy()
        if idx < 0 or idx > (len(tmp) - 1):
            return(tmp)
        else:
            tmp[idx] = element
            return (tmp)
