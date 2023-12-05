#!/usr/bin/python3
"""Module for lookup method"""


def lookup(obj):
    """look up object attreubutes and methods.
    Args:
        ob (object) : the object to list

    Returns:
        list: the list of attributes.
    """
    return dir(obj)
