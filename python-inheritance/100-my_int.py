#!/usr/bin/python3
"""Module that defines MyInt."""


class MyInt(int):
    """A rebel integer."""

    def __eq__(self, other):
        """Invert == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert != operator."""
        return super().__eq__(other)
