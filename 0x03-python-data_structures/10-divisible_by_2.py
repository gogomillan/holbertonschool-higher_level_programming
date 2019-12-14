#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return (None)
    ret = []
    for i in my_list:
        if (abs(i) % 2) == 0:
            ret.append(True)
        else:
            ret.append(False)
    return ret
