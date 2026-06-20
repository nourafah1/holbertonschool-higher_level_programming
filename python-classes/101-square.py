#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__position = value

    def area(self):
        """Return square area."""
        return self.__size ** 2

    def my_print(self):
        """Print square using #."""
        print(self)

    def __str__(self):
        """Return square representation."""
        if self.__size == 0:
            return ""

        square = "\n" * self.__position[1]

        for i in range(self.__size):
            square += (" " * self.__position[0]) + ("#" * self.__size)

            if i != self.__size - 1:
                square += "\n"

        return square
