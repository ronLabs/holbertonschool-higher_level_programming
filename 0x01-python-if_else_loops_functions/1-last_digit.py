#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strg1 = "Last digit of "
strg2 = " is "
greater = " and is greater than 5"
zero = " and is 0"
less = " and is less than 6 and not 0"

if number >= 0:
    ldigit = number % 10
if number < 0:
    ldigit = number % -10

if ldigit > 5:
    print("{}{:d}{}{:d}{}".format(strg1, number, strg2, ldigit, greater))
elif ldigit == 0:
    print("{}{:d}{}{:d}{}".format(strg1, number, strg2, ldigit, zero))
else:
    print("{}{:d}{}{:d}{}".format(strg1, number, strg2, ldigit, less))
