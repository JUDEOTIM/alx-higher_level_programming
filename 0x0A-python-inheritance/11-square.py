#!/usr/bin/python3
""" Square Module
Attributes:
    Rectangle (object): Base Object
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """ Square Class
    """

    def __init__(self, size: int) -> None:
        """ instance initialization function
        Args:
            size (int): Description
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self) -> str:
        return f"[Square] {self._Square__size:d}/{self._Square__size:d}"
