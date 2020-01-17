#!/usr/bin/python3
"""
Module for the add_atribute function
"""


def add_attribute(obj, name, value):
    """
    Function to set atributes in a object.

    Args:
        name (str): The name of the object
        value (object): The value of the object
    """
    if str(type(obj)).find("__main__") != -1:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
