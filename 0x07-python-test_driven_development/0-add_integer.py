#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Return the integer addtion of a and b.

    float arguments

    Raises:
    TypeError: If eitehr of a or b is a non-integer and non-float.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int , float):
        raise TypeError("b must be and integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
