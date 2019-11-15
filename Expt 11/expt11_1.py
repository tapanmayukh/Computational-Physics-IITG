import numpy as np


def gauss_siedel(a0, an, b0, bn, h):
	nx = int(abs(xn - x0) / h)
	ny = int(abs(yn - y0) / h)

	mat = np.zeros((nx + 1, ny + 1))
	mat[0] = a0
	mat[nx] = an
	
	mat[:, 0] = b0
	mat[:, ny] = bn
	
	err = np.ones_like(mat)
	k = 0
	
	while k < 8000:
		mat_old = mat
		for i in range(1, nx):
			for j in range(1, ny):
				mat[i, j] = 0.25 * (mat[i + 1, j] + mat[i - 1, j] + mat[i, j + 1] + mat[i, j - 1])
				if mat[i, j] != 0:
					err[i, j] = np.abs(mat_old[i, j] - mat[i, j]) / mat[i, j]
				
		k += 1
	
	return nx, ny, k, mat


def pred(x0, xn, y0, yn, h, mat, x, y):
	nx = int(abs(x - x0) / h)
	ny = int(abs(y - y0) / h)
	
	return mat[nx, ny]


if __name__ == "__main__":
	x0 = float(input("Enter the starting value of x     : "))
	a0 = float(input("Enter the starting value of f at x: "))
	
	xn = float(input("\nEnter the final value of x     : "))
	an = float(input("Enter the final value of f at x: "))
	
	y0 = float(input("\nEnter the starting value of y     : "))
	b0 = float(input("Enter the starting value of f at y: "))
	
	yn = float(input("\nEnter the final value of y     : "))
	bn = float(input("Enter the final value of f at y: "))
	
#	nx = float(input("\nEnter the number of divisions in x-dir: "))
#	ny = float(input("Enter the number of divisions in y-dir: "))

	h = float(input("\nEnter the division h: "))
	
	nx, ny, k, mat = gauss_siedel(a0, an, b0, bn, h)
	
	x = float(input("\nEnter the desired point x: "))
	y = float(input("Enter the desired point y: "))
	
	val = pred(x0, xn, y0, yn, h, mat, x, y)
	print("The value of f at ({}, {}) is: {}".format(x, y, val))
	
	with open("data1.dat", "w") as f:
		for i in range(nx + 1):
			for j in range(ny + 1):
				x = x0 + i * h
				y = y0 + j * h
				val = mat[i, j]
				
				f.write("{} {} {}\n".format(x, y, val))
