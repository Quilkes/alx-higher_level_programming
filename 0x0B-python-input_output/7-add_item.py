#!/usr/bin/python3
"""
7-save_to_json_file.py
save_to_json_file(my_obj, filename)
imports json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a file using JSON representation
    """
    with open(filename, "w") as fil:
        fil.write(json.dumps(my_obj))
