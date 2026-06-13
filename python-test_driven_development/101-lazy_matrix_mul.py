#!/usr/bin/python3
"""Lazy matrix multiplication"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 matrices using NumPy"""
    return np.matmul(m_a, m_b)
