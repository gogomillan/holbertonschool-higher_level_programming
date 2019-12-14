#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = None
    score = 0
    for k, v in a_dictionary.items():
        if v > score:
            best = k
            score = v
    return best
