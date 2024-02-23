#!/usr/bin/env python

"""Basic example

Demonstrates how to create symbols and print some algebra operations.
"""

from sympy import Symbol, Matrix


def mat2D():
	a = Symbol('a')
	b = Symbol('b')
	c = Symbol('c')
	d = Symbol('d')
	e = Symbol('e')
	f = Symbol('f')
	g = Symbol('g')
	h = Symbol('h')
	i = Symbol('i')
	M = Matrix(3, 3, [a, b, c, b, e , b, c, b , a])
	(P,D)=M.diagonalize(reals_only=False, sort=False, normalize=False)
	print(D)
    

if __name__ == "__main__":
    mat2D()
