#!/usr/bin/python3
"""Lazy matrix multiplication"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 matrices using NumPy"""
    if isinstance(m_a, str) or isinstance(m_b, str):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    return np.matmul(m_a, m_b)
