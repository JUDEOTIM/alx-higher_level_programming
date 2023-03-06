#!/usr/bin/python3
""" Myint Module
"""


class MyInt(int):

    """ My int object
    """

    def __eq__(self, other: object) -> bool:
        """ inverts the equality operator
        Args:
            other (object): Other object
        Returns:
            bool: True or false
        """
        return self - other != 0

    def __ne__(self, other: object) -> bool:
        """ inverts not equal operator
        Args:
            other (obj): Other object
        Returns:
            bool: True or false
        """
        return self - other == 0
