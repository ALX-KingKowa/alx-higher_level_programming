#!/usr/bin/python3
# 2-square.py
"""Defines a class Square."""


class Square:
    """Defines a class Square"""

    def __init__(self, size=0):
        """Initializes instance variable

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
