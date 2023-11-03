#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range matrix:
        for j in range matrix:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
