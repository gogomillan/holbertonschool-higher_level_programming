#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    import calculator_1 as c
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, c.add(a, b)))
    elif sys.argv[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, c.sub(a, b)))
    elif sys.argv[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, c.mul(a, b)))
    elif sys.argv[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, c.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
