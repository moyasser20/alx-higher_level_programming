#!/usr/bin/python3

def search_replace(my_list, search, replace):

    newm = []

    for element in my_list:
        if element == search:
            newm.append(replace)
        else:
            newm.append(element)
        retun newm

