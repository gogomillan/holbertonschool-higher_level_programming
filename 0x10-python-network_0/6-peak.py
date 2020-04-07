#!/usr/bin/python3
"""
Script for a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (int): Unrdered integer list to find the peak

    Returns:
        The peak value
    """
    lof = list_of_integers
    """ Special cases : no data, single element """
    if len(lof) == 0:
        return None
    if len(lof) == 1:
        return lof[0]

    """ Brute force
        Decide peak left edge
        Decide peak right edge
        Decide the peak against its neighbors
    """
    peak = 0
    for i in range(len(lof)):
        if i == 0 and lof[i] > lof[i + 1]:
            peak = lof[i] if lof[i] > peak else peak
        elif i == len(lof) - 1 and lof[i] > lof[i - 1]:
            peak = lof[i] if lof[i] > peak else peak
        elif (i == 0 or lof[i] >= lof[i - 1]) and (i == len(lof) - 1 or lof[i] >= lof[i + 1]):
            peak = lof[i] if lof[i] > peak else peak

    return peak

    """ Binary Searcha
        - Decides the middle element
        - elif lower half call
        - else higher half call
    mid = len(lof) // 2
    print("{}, ".format(lof[mid]), end="")
    if (mid == 0 or lof[mid - 1] <= lof[mid]) \
            and (mid == len(lof) - 1 or lof[mid + 1] <= lof[mid]):
        return lof[mid]
    elif lof[mid - 1] > lof[mid]:
        return(find_peak(lof[0:mid - 1]))
    else:
        return(find_peak(lof[mid:len(lof)]))
    """
