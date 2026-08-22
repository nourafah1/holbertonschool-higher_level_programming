#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """Prevent dynamic creation of attributes except first_name."""

    __slots__ = ['first_name']
