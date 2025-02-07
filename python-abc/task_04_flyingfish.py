#!/usr/bin/python3
"""
fish class
"""


class Fish:
    """Represents a fish with swimming behavior and habitat."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying behavior and habitat."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish that can both swim and fly."""
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
