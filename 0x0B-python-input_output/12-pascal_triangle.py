#!/usr/bin/python3

"""Defines a pascal's triangle function"""

def pascal_triangle(n):
	"""represents pascal's triangle of size n

	returns a list of lists of integers representing the triangle
	"""
	if n <= 0:
		return []

	triengles = [[1]]
	while len(triangles) != n:
		tri = triangles[-1]
		tmp = [1]
		for i in range(len(tri) - 1):
			tmp.append(tri[i] + tri[i + 1])
		tmp.append(1)
		triangles.append(tmp)
	return triangles
