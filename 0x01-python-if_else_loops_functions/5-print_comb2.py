#!/usr/bin/python3
# Program that prints numbers from 0 to 99
for num in range(0, 100):
    if num < 99:
        print('{:02d}, '.format(num), end='')
    if num in [99]:
        print('{:d}'.format(num))
