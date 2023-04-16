#!/usr/bin/python3
"""Define a class square."""

class Square:
	"""Represent a square."""

	def __init__(self,size=0):
		if not isinstance(size, int):
			raise TypeError("size must be integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size

	def area(self):
		""" return the current area of the sqaure"""
		return(self.__size * self.__size)
