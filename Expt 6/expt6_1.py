from math import sqrt, pi, sin, cos, atan


def matmul(A, B):
	assert(len(A[0]) == len(B))
	
	
	mat = [[0 for i in range(len(B[0]))] for j in range(len(A))]
	
	for i in range(len(A)):
		for j in range(len(B[0])):
			sum_ = 0
			for k in range(len(A[0])):
				sum_ += A[i][k] * B[k][j]
			mat[i][j] = sum_
	
	return mat


def transpose(A):
	mat = [[0 for i in range(len(A))] for j in range(len(A[0]))]
	
	for i in range(len(A)):
		for j in range(len(A[0])):
			mat[j][i] = A[i][j]
	
	return mat


def maxval(A):
	n = len(A)
	maxn = 0.0
	k, l = 0, 0
	
	for i in range(n - 1):
		for j in range(i + 1, n):
			if maxn <= abs(A[i][j]):
				maxn = abs(A[i][j])
				k = i
				l = j
	
	return maxn, k, l


def rotate(A, k, l, tol = 1.0e-9):
	n = len(A)
	diff = A[l][l] - A[k][k]
	
	if diff < tol:
		theta = pi / 4
	else:
		theta = 0.5 * atan(2 * A[k][l] / diff)
	
	s = sin(theta)
	c = cos(theta)
	
	rot = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		rot[i][i] = 1.0
	
	rot[k][k] = c
	rot[k][l] = s
	rot[l][k] = -s
	rot[l][l] = c
	
	rot_inv = transpose(rot)
	B = matmul(rot_inv, A)
	B = matmul(B, rot)
	
	print()
	for i in range(n):
		for j in range(n):
			print("{:-10f}".format(rot[i][j]), end = '')
		print(" || ", end = '')
		for j in range(n):
			print("{:-10f}".format(B[i][j]), end = '')
		print()
	
	return B, rot


def jacobi(A, tol = 1.0e-9):
	n = len(A)
	A = A[:]
	num_iter = 5 * (n ** 2)
	rot = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		rot[i][i] = 1.0
	
	print("\nIteration 0:")
	print()
	for i in range(n):
		for j in range(n):
			print("{:-10f}".format(rot[i][j]), end = '')
		print(" || ", end = '')
		for j in range(n):
			print("{:-10f}".format(A[i][j]), end = '')
		print()
	
	for i in range(num_iter):
		max_n, k, l = maxval(A)
		if max_n <= tol:
			return A, rot
		print("\nIteration {}:".format(i+1))
		A, x = rotate(A, k, l)
		
		rot = matmul(rot, x)
	
	print("\nJacobi Method didn't converge.")


if __name__ == "__main__":
#	n = int(input("Enter dimension of matrix: "))
	
	A = [[2, 3, 1], [3, 2, 2], [1, 2, 1]]
#	for i in range(n):
#		var = list(map(float, input("Enter Row {} of matrix: ".format(i+1)).split()))
#		A.append(var)

	n = len(A)
	D, S = jacobi(A)
	print("\nDiagonal Matrix:")
	for i in range(n):
		for j in range(n):
			print("{:-10f}".format(D[i][j]), end = '')
		print()
	print("\nRotation Matrix:")
	for i in range(n):
		for j in range(n):
			print("{:-10f}".format(S[i][j]), end = '')
		print()
	print("\nEigenvalues: ", end = '')
	for i in range(n):
		print("{:-10f}".format(D[i][i]), end = '\t')
	print()
	
	print("\nEigenvectors:")
	for i in range(n):
		print("\n[\t", end = '')
		for j in range(n):
			print("{:-10f}".format(S[j][i]), end = '\t')
		print("]")
