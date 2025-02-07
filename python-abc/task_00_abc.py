#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    All subclasses must implement the sound method.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by subclasses
        to return the animal's sound.
        """
        pass


class Dog(Animal):
    """
    Dog class inheriting from Animal.
    """
    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class inheriting from Animal.
    """
    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"
