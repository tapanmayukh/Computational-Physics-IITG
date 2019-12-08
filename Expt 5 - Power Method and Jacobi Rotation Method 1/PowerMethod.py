# Finding largest Eigenvalue and corresponding Eigenvector using Power Method.

# Tapan Mayukh - 170121048 - 02/09/2019


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


def dot(A, B):
	assert(len(A[0]) == 1)
	assert(len(B[0]) == 1)
	assert(len(A) == len(B))
	
	pr = 0
	for i in range(len(A)):
		pr += A[i][0] * B[i][0]
	
	return pr


def normalize(A):
	n = len(A)
	
	A = A[:]
	max_n = A[0][0]
	for i in range(n):
		if max_n < A[i][0]:
			max_n = A[i][0]
	
	for i in range(n):
		A[i][0] /= max_n
		
	return A


def power(A, x, tol = 1.0e-5):
	n = len(A)
	
	mat_n = x
	mat_n_1 = matmul(A, x)
	
	val_n = dot(mat_n, mat_n)
	val_n_1 = dot(mat_n_1,  mat_n)
	
	l_n = 1.0e-8
	l_n_1 = val_n_1 / val_n
	n = 1
	print("\nIteration {}: Eigenvalue: {} Eigenvector: {}".format(n, l_n_1, normalize(mat_n_1)))
	
	while abs(l_n_1 - l_n) > tol:
		mat_n = mat_n_1
		mat_n_1 = matmul(A, mat_n)
	
		val_n = dot(mat_n, mat_n)
		val_n_1 = dot(mat_n_1,  mat_n)
	
		l_n = l_n_1
		l_n_1 = val_n_1 / val_n
		
		n += 1
		print("\nIteration {}: Eigenvalue: {} Eigenvector: {}".format(n, l_n_1, normalize(mat_n_1)))
	
	mat_n_1 = normalize(mat_n_1)
	return l_n_1, mat_n_1


def del_matrix(matrix, r, c):
	del_mat = [[0 for i in range(len(matrix) - 1)] for i in range(len(matrix[0]) - 1)]
	
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if i < r and j < c:
				del_mat[i][j] = matrix[i][j]
			elif i < r and j > c:
				del_mat[i][j - 1] = matrix[i][j]
			elif i > r and j < c:
				del_mat[i - 1][j] = matrix[i][j]
			elif i > r and j > c:
				del_mat[i - 1][j - 1] = matrix[i][j]
	
	return del_mat


def determinant(matrix):
	if len(matrix) == 1:
		return matrix[0][0]
	elif len(matrix) == 2:
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	
	det = 0
	
	for i in range(len(matrix[0])):
		det += pow(-1, i) * matrix[0][i] * determinant(del_matrix(matrix, 0, i))
	
	return det


if __name__ == "__main__":
	n = int(input("Enter dimension of matrix: "))
	
	A = []
	trace = 0
	for i in range(n):
		var = list(map(float, input("Enter Row {} of matrix: ".format(i+1)).split()))
		A.append(var)
		trace += A[i][i]
	
	print("\nDeterminant: {}\nTrace: {}".format(determinant(A), trace))
	
	print()
	x = []
	for i in range(n):
		var = list(map(float, input("Enter Row {} of starting vector: ".format(i+1)).split()))
		x.append(var)
	
	l, v = power(A, x)
	print("\nEigenvalue: {:-5.3f}".format(l))
	print("Eigenvector:")
	
	for i in range(len(v)):
		print("\t{:-8.3f}".format(v[i][0]))
	print()
