#!/usr/bin/python3
import sys

def add_arguments(arguments):
    result = 0
    for arg in arguments:
        result += int(arg)
    return result

if __name__ == '__main__':
    arguments = sys.argv[1:]
    total = add_arguments(arguments)
    print(total)
