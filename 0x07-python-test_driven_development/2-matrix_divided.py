#!/usr/bin/python3
""" Matrix Divided Module
"""


def matrix_divided(matrix, div):
    """ Divides all the items of the sub lists by the div
    Args:
        matrix (list): list of list
        div (int or float): The dividend param
    Returns:
        list: the resulting list
    Raises:
        TypeError: matrix must be a matrix list of list
        ZeroDivisionError: division error
    """
    if not isinstance(matrix, list) or matrix == [] or \
            not all(isinstance(mat, list) for mat in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for mat in matrix:
        if not all(isinstance(item, int) or
                   isinstance(item, float) for item in mat):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    if not all(len(mat) == len(matrix[0]) for mat in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float) or \
            isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for mat in matrix:
        new_matrix.append(list(map(lambda item: round(item/div, 2), mat)))

    return new_matrix
