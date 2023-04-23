#!/usr/bin/python3
"""Defiens an inherited list class mylist"""

class MyList(list):
    """implements sorted printing for the built-in list class"""
    def print_sorted(self):
        """print a list of sorted ascending order"""
        print(sorted(self))
