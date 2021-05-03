#addition for a curve y^2 = x^3 + Ax + B
from fractions import Fraction
import math
import time

A = int(input ('input A for the curve'))
B = int(input ('input B'))
x = int(input ('start x coor:'))
y = int(input ('start y coor:'))

iterations = input('iterations ?')
x = Fraction(x)
y = Fraction(y)

#The below loop simply doubles the base point
for i in range(1):
	l = Fraction((3*(x**2) + A)/(2*y))
	nu = Fraction((-x**3 + A*x + 2*B)/(2*y))
	x_2 = Fraction(l**2 -  2*x)
	y_2 = Fraction(-l**3 + l*2*x - nu)
	#y_2 = Fraction(y + l*(x_2 - x))
	height = max(x_2.numerator,x_2.denominator)
	print (height)

#This loop generates 3P, 4P, 5P and so on
for j in range(int(iterations)):
	x_old = x
	y_old = y
	l = Fraction((y_2-y)/(x_2-x))
	nu = Fraction((y*x_2 - y_2*x)/(x_2-x))
	y_2 = -l**3 + l*(x_old + x_2) - nu
	x_2 = l**2 - x_old - x_2
	height = max(x_2.numerator,x_2.denominator)
	print (height)

