#!/usr/bin/python3
for alphab in range(97, 123):
    if alphab == 101 or alphab == 113: #if alphab in [101, 103].. other way
        continue
    print('{:c}'.format(alphab), end='')
