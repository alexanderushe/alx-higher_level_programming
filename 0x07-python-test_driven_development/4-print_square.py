#!/usr/bin/python3

def print_square(size):
    if not isinstance(size, (int,float)):
        raise TypeError("size must be an integer")
    elif size < 0
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
    size = int(size) #if size is a float convert it
    i = 0

    for i in range(0, size):
        j = 0
        for j in range(0, size):
            print('#', end='')
        print()
