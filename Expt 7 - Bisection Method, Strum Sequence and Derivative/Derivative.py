# Finding the derivative and double derivative of a function

# Tapan Mayukh - 170121048 - 23/09/2019

from math import sinh, tanh


def derivate(func, val):
	h = pow(10, -9)
	d = (func(val + h) - func(val)) / h
	
	return d
	

def dbl_derivate(func, val):
	h = pow(10, -4)
	d = (func(val + 2 * h) - 2 * func(val + h) + func(val)) / (h * h)
	return d


if __name__ == "__main__":
	x = 0.5
	
	d1 = derivate(sinh, x)
	d2 = derivate(tanh, x)
	d3 = dbl_derivate(sinh, x)
	d4 = dbl_derivate(tanh, x)
	
	print("Derivative of sinh at x = {}: {}".format(x, d1))
	print("Derivative of tanh at x = {}: {}".format(x, d2))
	print("Double Derivative of sinh at x = {}: {}".format(x, d3))
	print("Double Derivative of tanh at x = {}: {}".format(x, d4))
