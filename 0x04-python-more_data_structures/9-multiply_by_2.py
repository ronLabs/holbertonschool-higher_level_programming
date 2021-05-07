#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    double = (lambda x: (x[0], x[1] * 2))
    b_dictionary = dict(map(double, a_dictionary.items()))
    return (b_dictionary)
