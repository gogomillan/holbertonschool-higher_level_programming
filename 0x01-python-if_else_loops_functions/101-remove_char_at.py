#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    s = ""
    for x in str:
        if i != n:
            s = s + x
        i = i + 1

    return (s)
