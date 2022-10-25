#!/usr/bin/python3
"""
Contains the "read_lines" function
"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        i = 0
        for i, line in enumerate(f):
            if i == nb_lines:
                break
            print(line, end='')
