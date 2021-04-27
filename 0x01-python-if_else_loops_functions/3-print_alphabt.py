#!/usr/bin/python3
for alphab in range(97, 123):
    # if alphab in [101, 103].. other way
    if alphab == 101 or alphab == 113:
        continue
    print('{:c}'.format(alphab), end='')
