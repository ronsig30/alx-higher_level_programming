#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for colum in i:
            print("{:d}".format(colum), end=" " if colum != i[-1] else "")
        print()
