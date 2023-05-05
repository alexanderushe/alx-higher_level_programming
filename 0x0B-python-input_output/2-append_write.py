#!/usr/bin/python3

"""appends text at the end of a text file"""

def append_write(filename="", text=""):
    """returns appended text"""
    with open(filename, 'a', encoding= 'utf-8') as f:
        return f.write(text)
