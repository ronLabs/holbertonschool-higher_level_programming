#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    str1 = "argument"
    str2 = "arguments"
    l = (len(sys.argv) - 1)

    if l == 1:
        print("{:d} {}:".format(l, str1))
    elif l == 0:
        print("{:d} {}.".format(l, str2))
    else:
        print("{:d} {}:".format(l, str2))

    for index in range(1, l + 1):
        print("{:d}: {}".format(index, sys.argv[index]))
