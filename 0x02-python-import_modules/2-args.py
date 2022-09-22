#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    print("{:d} argument".format(argc), end='')
    if argc == 0:
        print("s.")
    elif argc == 1:
        print(":")
    else:
        print("s:")
    for num in range(1, argc + 1):
        print("{:d}: {:s}".format(num, argv[num]))
