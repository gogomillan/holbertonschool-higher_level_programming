#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if __name__ != '__main__':
        if matrix is None:
            return
        for elem in matrix:
            ctrl = 0
            for num in elem:
                if ctrl != 0:
                    print(" ", end="")
                print("{:d}".format(num), end="")
                ctrl += 1
            print()
