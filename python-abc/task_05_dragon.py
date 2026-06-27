#!/usr/bin/env python3
"""Module that demonstrates mixins."""


class SwimMixin:
    """Mixin that adds swimming ability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon."""

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")
