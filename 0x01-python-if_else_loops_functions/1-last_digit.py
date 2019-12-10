#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = abs(number) % 10 * (-1 if number < 0 else 1)
if (lastdig > 5):
    print("The last digit of {} is {} and is greater than 5".format(number,
                                                                    lastdig))
elif (lastdig == 0):
    print("The last digit of {} is {} and is 0".format(number, lastdig))
else:
    print("The last digit of {} is {} \
and is less than 6 and not 0".format(number, lastdig))
