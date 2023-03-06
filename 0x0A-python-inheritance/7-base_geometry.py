#!/usr/bin/python3
""" Base Geometry Class module
"""


class BaseGeometry:

    """ Base Geometry Class
    """

    def area(self) -> Exception:
        """ area method not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> Exception:
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
