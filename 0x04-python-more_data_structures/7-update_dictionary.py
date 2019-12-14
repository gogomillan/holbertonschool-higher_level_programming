#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    flag = True
    for k, v in a_dictionary.items():
        if k == key:
            a_dictionary[k] = value
            flag = False
    if flag:
        a_dictionary[key] = value
    return a_dictionary
