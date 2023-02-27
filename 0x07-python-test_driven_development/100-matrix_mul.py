#!/usr/bin/python3
"""Defines a matrix multiplying module."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    a = [x for row in m_a for x in row]
    if not all((isinstance(ele, int) or isinstance(ele, float)) for ele in a):
        raise TypeError("m_a should contain only integers or floats")

    b = [x for row in m_b for x in row]
    if not all((isinstance(ele, int) or isinstance(ele, float)) for ele in b):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invert_m_b = []
    for row in range(len(m_b[0])):
        new_row = []
        for col in range(len(m_b)):
            new_row.append(m_b[col][row])
        invert_m_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in invert_m_b:
            mul = 0
            for index in range(len(m_a[0])):
                mul += row[index] * col[index]
            new_row.append(round(mul, 2))
        new_matrix.append(new_row)

    return (new_matrix)
