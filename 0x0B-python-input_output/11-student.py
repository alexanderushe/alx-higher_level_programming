#!/usr/bin/python3

"""Module that defines the class student
"""

class Student:
	"""class to create a student instance"""

	def __init__(self, first_name, last_name, age):
		"""specail method to initialize"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self, attrs=None):
		"""Method that returns directory description"""
		obj = self.__dict__.copy()
		if type(attrs) is list:

			for item in attrs:
				if type(item) is not str:
					return obj

			d_list = {}

			for iatr in range(len(attrs)):
				for satr in obj:
					if attrs[iatr] == satr:
						d_list[satr] = obj[satr]
			return d_list
		return obj
	def reload_from_json(self, json):
		"""replace all attributes of the student instance"""
		for atr in json:
			self.__dict__[atr] = json[atr]
