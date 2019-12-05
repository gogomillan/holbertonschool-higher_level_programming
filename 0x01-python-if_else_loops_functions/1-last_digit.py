#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number - (int(number / 10)) * 10
if mod == 0:
    msg = "and is 0"
elif mod > 5:
    msg = "and is greater than 5"
else:
    msg = "and is less than 6 and not 0"
print("Last digit of", "{:d}".format(number), "is {:d}".format(mod), msg)
