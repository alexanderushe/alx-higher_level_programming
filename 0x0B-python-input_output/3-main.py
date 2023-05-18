#!/usr/bin/python3
write_file = __import__('3-to_json_string.py').write_file

nb_characters = write_file("my_first_file.txt", "Holberton School is so cool!\n")
print(nb_characters)
