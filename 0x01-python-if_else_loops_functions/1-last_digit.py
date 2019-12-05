#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
module = number - (int(number / 10)) * 10
if module == 0:
	print("Last digit of {:d} is {:d} is zero".format(number, module))
elif module > 5:
	print("Last digit of {:d} is {:d} and is greater than 5".format(number, module))
else:
	print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, module))
