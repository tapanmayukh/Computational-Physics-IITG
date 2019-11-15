from math import sqrt


def maxval(A):
	n = len(A)
	
	max_n = 0.0
	k, l = 0, 0
	
	for i in range(n - 1):
		for j in range(i + 1, n):
			if max_n <= abs(A[i][j]):
				max_n = abs(A[i][j])
				k = i
				l = j
	
	return max_n, k, l


def rotate(A, rot, k, l):
	n = len(A)
	diff = A[l][l] - A[k][k]
	
	if abs(A[k][l]) < abs(diff) * 1.0e-36:
		t = A[k][l] / diff
	else:
		phi = diff / (2.0 * A[k][l])
		t = 1.0 / (abs(phi) + sqrt(phi ** 2 + 1.0))
		
		if phi < 0.0:
			t = -t
	
	c = 1.0 / (sqrt(t ** 2 + 1.0))
	s = t * c
	
	tau = s / (1.0 + c)
	# print(c, s, t, tau)
	
	temp = A[k][l]
	A[k][l] = 0.0
	A[l][k] = 0.0
	A[k][k] -= t * temp
	A[l][l] += t * temp
	
	for i in range(k):
		temp = A[i][k]
		A[i][k] -= s * (A[i][l] + tau * temp)
		A[i][l] += s * (temp - tau * A[i][l])
	
	for i in range(k + 1, l):
		temp = A[k][i]
		A[k][i] -= s * (A[i][l] + tau * temp)
		A[i][l] += s * (temp - tau * A[i][l])
	
	for i in range(l + 1, n):
		temp = A[k][i]
		A[k][i] -= s * (A[l][i] + tau * temp)
		A[l][i] += s * (temp - tau * A[l][i])
	
	for i in range(n):
		temp = rot[i][k]
		rot[i][k] -= s * (rot[i][l] + tau * temp)
		rot[i][l] += s * (temp - tau * rot[i][l])


def jacobi(A, tol = 1.0e-9):
	n = len(A)
	A = A[:]
	num_iter = 5 * (n ** 2)
	
	rot = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		rot[i][i] = 1.0
	
	for i in range(num_iter):
		max_n, k, l = maxval(A)
		if max_n <= tol:
			return A, rot
		rotate(A, rot, k, l)
	
	print("\nJacobi Method didn't converge.")


if __name__ == "__main__":
	n = int(input("Enter dimension of matrix: "))
	
	A = []
	for i in range(n):
		var = list(map(float, input("Enter Row {} of matrix: ".format(i+1)).split()))
		A.append(var)

	D, S = jacobi(A)
	print("\nDiagonal Matrix:")
	for i in range(n):
		for j in range(n):
			print("{:-10.3f}".format(D[i][j]), end = '')
		print()
	print("\nRotation Matrix:")
	for i in range(n):
		for j in range(n):
			print("{:-10.3f}".format(S[i][j]), end = '')
		print()
