#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    values = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    summ = 0
    val = 0
    for k in roman_string:
        if values[k] > val:
            summ = summ + values[k] - val * 2
        else:
            summ = summ + values[k]
        val = values[k]
    return summ
