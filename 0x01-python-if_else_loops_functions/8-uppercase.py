#!/usr/bin/python3
def uppercase(str):
    for check in str:
        for letter in range(97, 123):
            if letter == ord(check):
                check = chr(letter - 32)
        print("{:s}".format(check), end='')
    print("")
