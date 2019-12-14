#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return None
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    summ = 0
    val = 0
    for k in roman_string:
        if values[k] > val:
            summ = values[k] - summ
        else:
            summ = summ + values[k]
        val = values[k]
    return summ
