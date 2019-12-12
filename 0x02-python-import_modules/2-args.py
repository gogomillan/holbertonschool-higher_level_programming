#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        print("{:d} argument.".format(len(sys.argv)-1))
    else:
        print("{:d} arguments.".format(len(sys.argv)-1))
    i = 0
    for arg in sys.argv[1:]:
        i = i + 1
        print("{:d}: {}".format(i, arg))
