# Linear Congruential Generator of Random values for 2-D integration
# Initialization with different seeds

# Tapan Mayukh - 170121048 - 18/11/2019

import numpy as np


def LCG(n, x0, t0, t1):
	m = 714025
	a = 1366
	c = 150889
	
	random_nos = []
	
	for i in range(n):
		xn = (a * x0 + c) % m
		random_nos.append(xn)
		
		x0 = xn
	
	random_nos = np.array(random_nos)
	random_nos = (t1 - t0) * random_nos / np.max(random_nos) + t0
	
	return random_nos
	

def fun(x, y):
	return x * x + y * y


def Monte_Carlo_int(n, t0, t1, y0, y1):
	V = (t1 - t0) * (y1 - y0)
	
	random_nos_x = LCG(n, 1, t0, t1)
	random_nos_y = LCG(n, 2, y0, y1)
	
	with open("data1.dat", "w") as f:
		for i in range(n):
			f.write("{} {}\n".format(random_nos_x[i], random_nos_y[i]))
	
	intg = np.sum(fun(random_nos_x, random_nos_y)) * V / n
	
	return intg


if __name__ == "__main__":
	n = 1000
	
	t0 = 0.0
	t1 = 1.0
	
	y0 = 0.0
	y1 = 1.0
	
	intg = Monte_Carlo_int(n, t0, t1, y0, y1)
	
	print("Integral of the function with {} random points in ({}, {}) X ({}, {}): {}".format(n, t0, t1, y0, y1, intg))
