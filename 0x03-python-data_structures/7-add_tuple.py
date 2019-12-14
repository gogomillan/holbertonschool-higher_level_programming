#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = [0, 0]
    for i in range(len(tuple_a)):
        c[i] = c[i] + tuple_a[i]
    for i in range(len(tuple_b)):
        c[i] = c[i] + tuple_b[i]
    return (tuple(c))
