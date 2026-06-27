#!/usr/bin/python3
"""Module that defines a Square class."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(
            self.__size,
            self.__size
        )
