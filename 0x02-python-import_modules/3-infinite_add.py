#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = (len(sys.argv) - 1)
    suma = 0
    for index in range(1, l + 1):
        suma = suma + int(sys.argv[index])
    print('{:d}'.format(suma))
