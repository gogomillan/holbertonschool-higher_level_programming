#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = [0, 0]
    limit = len(tuple_a) if len(tuple_a) <= 2 else 2
    for i in range(limit):
        c[i] = c[i] + tuple_a[i]
    limit = len(tuple_b) if len(tuple_b) <= 2 else 2
    for i in range(limit):
        c[i] = c[i] + tuple_b[i]
    return (tuple(c))
