#!/usr/bin/python3

"""writes a string to a text file and returns the number of characters"""

def write_file(filename="", text=""):
	""" write a string to a utf8 text file
	Args:
		filename (str): the name of the file to write.
		text (str): thee text to write to the file
	returns:
		the number of characters writtten
	"""
	with open(filename, "w", encoding="utf-8") as f:
		return f.write(text)
