#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences
    of an element by another in a new list
    """

    newm = []
    for element in my_list:
        if element == search:
            newm.append(replace)
        else:
            newm.append(element)
    return newm

