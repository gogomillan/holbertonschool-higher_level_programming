#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    summ = 0
    for i in my_set:
        summ = summ + i
    return summ
