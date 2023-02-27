#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (matmul(m_a, m_b))
