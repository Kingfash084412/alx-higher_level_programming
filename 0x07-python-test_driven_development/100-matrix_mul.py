#!/usr/bin/python3
"""
Function(s):
    matrix_mul: Multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """Recieves to matrices and multiplies them.

    Notes:
        This is just the begining edge cases. No math... yet.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")

    length = len(m_a[0])
    for i in m_a:
        if length != len(i):
            raise TypeError("each row of m_a must should be of the same size")
    length = len(m_b[0])
    for i in m_b:
        if length != len(i):
            raise TypeError("each row of m_b must should be of the same size")
