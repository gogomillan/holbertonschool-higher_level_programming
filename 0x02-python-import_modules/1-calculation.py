#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as c
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, c.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, c.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, c.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, c.div(a, b)))
