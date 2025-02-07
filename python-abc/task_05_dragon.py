#!/usr/bin/python3
"""
dragon
"""


class SwimMixin:
    """Mixin providing swimming ability."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying ability."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon that can both swim and fly."""
    def roar(self):
        print("The dragon roars!")
