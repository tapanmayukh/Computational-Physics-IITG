# Linear Congruential Generator of Random values for 1-D integration

# Tapan Mayukh - 170121048 - 18/11/2019

import numpy as np


def LCG(n, t0, t1):
	m = 714025
	a = 1366
	c = 150889
	
	x0 = 1
	
	random_nos = []
	
	for i in range(n):
		xn = (a * x0 + c) % m
		random_nos.append(xn)
		
		x0 = xn
	
	random_nos = np.array(random_nos)
	random_nos = (t1 - t0) * random_nos / np.max(random_nos) + t0
	
	return random_nos
	

def fun(x):
	return x * x


def Monte_Carlo_int(n, t0, t1):
	V = t1 - t0
	
	random_nos = LCG(n, t0, t1)
	with open("data.dat", "w") as f:
		for i in range(n):
			f.write("{} {}\n".format(i + 1, random_nos[i]))
	
	intg = np.sum(fun(random_nos)) * V / n
	
	return intg


if __name__ == "__main__":
	n = 1000
	
	t0 = 0.0
	t1 = 1.0
	
	intg = Monte_Carlo_int(n, t0, t1)
	
	print("Integral of the function with {} random points in ({}, {}): {}".format(n, t0, t1, intg))
