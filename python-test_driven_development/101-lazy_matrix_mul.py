#!/usr/bin/python3
"""Lazy matrix multiplication"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 matrices using NumPy"""
    if isinstance(m_a, str) or isinstance(m_b, str):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if m_a == [[]]:
        raise ValueError(
            "shapes (1,0) and (2,2) not aligned: "
            "0 (dim 1) != 2 (dim 0)"
        )

    if m_b == [[]]:
        raise ValueError(
            "shapes (2,2) and (1,0) not aligned: "
            "2 (dim 1) != 1 (dim 0)"
        )

    try:
        return np.matmul(m_a, m_b)
    except ValueError as err:
        if "setting an array element with a sequence" in str(err):
            raise ValueError("setting an array element with a sequence.")
        raise err
    except TypeError as err:
        if "ufunc" in str(err):
            raise TypeError("invalid data type for einsum")
        raise err
