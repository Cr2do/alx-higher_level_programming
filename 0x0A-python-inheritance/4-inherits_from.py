#!/usr/bin/python3
"""Module to checked inherit from"""


def inherits_from(obj, a_class):
    """Function that do the Job"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
