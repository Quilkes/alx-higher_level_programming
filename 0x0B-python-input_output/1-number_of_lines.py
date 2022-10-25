#!/usr/bin/python3
"""
1-number_of_lines.py
number_of_lines(filename="")
"""


def number_of_lines(filename=""):
    """
    Returns the number of lines of a text file
    """
    count = 0
    with open(filename) as fil:
        for line in fil:
            count += 1
    return count
