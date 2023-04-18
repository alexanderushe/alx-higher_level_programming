#!/usr/bin/python3
"""Defines a class square"""

class Square:
    """represents a square"""
    def __init__(self, size = 0):
        """initializes a new square
        size(int): the size of the new square
        """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >=0")
        self.__size = value

    def area(self):
        """return the current area of the square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defin the comparison to a square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a square"""
        return self.area() <= other.area()

    def __gt__(self,other):
        """Define the > comparison to a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a square"""
        return self.area() >= other.area()
