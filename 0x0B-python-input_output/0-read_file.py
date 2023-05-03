#!/usr/bin/python3

""" Defines a text file reading function"""

def read_file(filename=""):
    """reads a file of content utf-8 to stdout"""
    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end="")
