#!/usr/bin/python3
"""Define classes for a singly list"""

class Node:
	"""Represent  a node in a singly lnked list"""
	def __init__(self, data, next_node =None):
		"""initialize a new node.
		data (int) : the data of the new node
		next_node: next node of the new node.
		"""
		self.data = data
		self.next_node = next_node

	@property
	def data(self):
		"""Get/set data of node"""
		return (self.__data)

	@data.setter
	def data(self, value):
		if not isinstance(value, int):
			raise TypeError("data must be an integer")
		self.__data = value

	@property
	def next_node(self):
		"""Get/set the next_node of the node"""
		return(self.__next_node)

	@next_node.setter
	def next_node(self, value):
		if not isinstance(value, Node) and value is not None:
			raise TypeError("next_node must be a Node object")
		self.__next_node = value

class SinglyLinkedList:
	"""Represent a singly linked list"""

	def __init__(self):
		"""initialize new singlylinkedlist"""
		self.__head = None

	def sorted_insert(self, value):
		"""Insert a new node to the singlylinkedlist.
		the node is inserted into the list at the correct
		ordered numerical position.
		value(Node): new node to insert"""
		new = Node(value)
		if self.__head is None:
			new.next_node = None
			self.__head = new
		elif self.__head.data > value:
			new.next_node = self.__head
			self.__head = new
		else:
			tmp = self.__head
			while (tmp.next_node is not None and
				tmp.next_node.data < value):
				tmp = tmp.next_node
			new.next_node = tmp.next_node
			tmp.next_node = new

	def __str__(self):
		"""Define the print() representation of a singlylinkedlist"""
		values = []
		tmp = self.__head
		while tmp is not None:
			values.append(str(tmp.data))
			tmp = tmp.next_node
		return ('\n' .join(values))
