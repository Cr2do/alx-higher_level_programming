#!/usr/bin/python3
import random


number = random.randint(-10000, 10000)
valueGlobal = "Last digit of {}"
if number % 10 > 5:
    greaterVal = "is {} and is greater than 5"
    print(valueGlobal.format(number), greaterVal.format(number % 10))
elif number % 10 == 0:
    zeroVal = "is {} and is 0"
    print(valueGlobal.format(number), zeroVal.format(number % 10))
else:
    lowerVal = "is {} and is less than 6 and not 0"
    print(valueGlobal.format(number), lowerVal.format(number % 10))
