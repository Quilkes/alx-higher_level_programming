#!/usr/bin/python3
"""
7-base_geometry.py
class BaseGeometry
"""


class BaseGeometry:
    """
    Checks if value is valid and has an area that raises an error
    """
    def area(self):
        """
        Raises an exception error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
