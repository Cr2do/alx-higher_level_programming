#!/usr/bin/python3
"""
add_integer module
"""


def add_integer(a, b=98):
    """ add_integer
    Args:
        a: first parameter
        b: second parameter
    Returns:
        result a sum
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
