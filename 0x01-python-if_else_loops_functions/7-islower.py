#!/usr/bin/python3
"""Write a function that prints a string in lowercase followed by a new line."""

def islower(strr):
    if ord(strr) >= 97 and ord(strr) <= 122:
        return True
    else:
        return False
