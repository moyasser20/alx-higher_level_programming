#!/usr/bin/python3


def uniq_add(my_list=[]):

    newl = []
    sum = 0

    for num in my_list:
        if num not in newl:
            sum += num
            newl.append(num)
    return sum
