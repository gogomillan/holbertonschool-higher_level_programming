#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if (x % 3 == 0) and (x % 5 == 0):
            prn = "FizzBuzz "
        elif (x % 3 == 0):
            prn = "Fizz "
        elif (x % 5 == 0):
            prn = "Buzz "
        else:
            prn = str(x) + " "
        print("{}".format(prn), end='')
