#!/usr/bin/python3
""" Rectangle Module
Attributes:
    BaseGeometry (object): Base Geometry class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """ Rectangle Object
    """

    def __init__(self, width: int, height: int) -> None:
        """ Instantiation function
        Args:
            width (int): width arg
            height (int): height arg
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self) -> int:
        return self.__height * self.__width

    def __str__(self) -> str:
        return f"[Rectangle] {self.__width:d}/{self.__height:d}"
