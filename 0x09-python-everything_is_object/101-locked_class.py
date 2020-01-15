#!/usr/bin/python3
"""
Module for LockedClass with no class or object attribute.
"""


class LockedClass:
    def __setattr__(self, key, value):
        if key is not "first_name":
            raise AttributeError("'LockedClass' object has no attribute\
 'last_name'")
        object.__setattr__(self, key, value)
