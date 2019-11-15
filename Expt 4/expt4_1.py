def permute(n, A, b):
	for i in range(n):
		if A[i][i] == 0:
			for j in range(i, n):
				if A[j][j] != 0:
					break
			A[i], A[j] = A[j], A[i]
			b[i], b[j] = b[j], b[i]
	
	return A, b

'''
def decompose(n, A):
	L = [[0 for _ in range(n)] for __ in range(n)]
	U = [[0 for _ in range(n)] for __ in range(n)]
	
	for i in range(n):
		for k in range(i, n):
			
			s = 0
			for j in range(i):
				s += L[i][j] * U[j][k]
			U[i][k] = A[i][k] - s
		
		for k in range(i, n):
			if i == k:
				L[i][i] = 1
			else:
				s = 0
				for j in range(i):
					s += L[k][j] * U[j][i]
				L[k][i] = (A[k][i] - s) / U[i][i]
	
	return L, U
'''

def del_matrix(matrix, r, c):
	del_matrix = [[0 for i in range(len(matrix) - 1)] for i in range(len(matrix[0]) - 1)]
	
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if i < r and j < c:
				del_matrix[i][j] = matrix[i][j]
			elif i < r and j > c:
				del_matrix[i][j - 1] = matrix[i][j]
			elif i > r and j < c:
				del_matrix[i - 1][j] = matrix[i][j]
			elif i > r and j > c:
				del_matrix[i - 1][j - 1] = matrix[i][j]
	
	return del_matrix


def determinant(matrix):
	if len(matrix) == 1:
		return matrix[0][0]
	elif len(matrix) == 2:
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	
	det = 0
	
	for i in range(len(matrix[0])):
		det += pow(-1, i) * matrix[0][i] * determinant(del_matrix(matrix, 0, i))
	
	return det


def decompose(n, A):
	L = [[0 for _ in range(n)] for __ in range(n)]
	U = [[0 for _ in range(n)] for __ in range(n)]
	
	detL = 1
	detU = 1
	for i in range(n):
		L[i][i] = 2
		detL *= 2
		for k in range(i, n):
			s = 0
			for j in range(i):
				s += L[i][j] * U[j][k]
			U[i][k] = (A[i][k] - s) / L[i][i]
			if i == k:
				detU *= U[i][i]
		
		for k in range(i, n):
			if i != k:
				s = 0
				for j in range(i):
					s += L[k][j] * U[j][i]
				L[k][i] = (A[k][i] - s) / U[i][i]
	
	
	print("\nDeterminant of L: {}\nDeterminant of U: {}\nDeterminant of L * U: {}".format(detL, detU, detL * detU))
	print("\nDetreminant of A: {}".format(determinant(A)))
	
	return L, U

'''
def decompose(n, A):
	L = [[0 for _ in range(n)] for __ in range(n)]
	U = [[0 for _ in range(n)] for __ in range(n)]
	
	for i in range(n):
		for k in range(i + 1):
			
			s = 0
			for j in range(k):
				s += L[i][j] * U[j][k]
			L[i][k] = A[i][k] - s
		
		for k in range(i, n):
			if i == k:
				U[i][i] = 1
			else:
				s = 0
				for j in range(i):
					s += U[j][k] * L[i][j]
				U[i][k] = (A[i][k] - s) / L[i][i]
	
	return L, U
'''

def forward_substitute(n, A, b):
	y = [[0] for _ in range(n)]
	
	for i in range(n):
		t = 0
		for j in range(i):
			t += y[j][0] * A[i][j]
		
		y[i][0] = (b[i][0] - t) / A[i][i]
	
	return y


def back_substitute(n, A, b):
	ans = [[0] for i in range(n)]
	
	for i in range(n-1, -1, -1):
		t = 0
		for j in range(i + 1, n):
			t += ans[j][0] * A[i][j]
		
		ans[i][0] = (b[i][0] - t) / A[i][i]
	
	return ans	


if __name__ == "__main__":
	n = int(input("Enter the number of equations: "))
	A = []
	b = []
	
	for i in range(n):
		var = list(map(int, input("Enter Row {} of coefficient matrix: ".format(i+1)).split()))
		A.append(var)
	for i in range(n):
		var = list(map(int, input("Enter Row {} of constant vector: ".format(i+1)).split()))
		b.append(var)
	
	A, b = permute(n, A, b)
	L, U = decompose(n, A)

	print('\nLower Triangular Matrix:')
	for l in range(n):
		for k in range(n):
			print('{:-7.2f}'.format(L[l][k]), end=' ')
		print('')
	print()

	print('Upper Triangular Matrix:')
	for l in range(n):
		for k in range(n):
			print('{:-7.2f}'.format(U[l][k]), end=' ')
		print('')
	print()

	y = forward_substitute(n, L, b)
	print("\nY_vector:")
	for k in range(len(y)):
		print('{:-7.2f}'.format(y[k][0]), end=' ')
	print()
	
	ans = back_substitute(n, U, y)
	print("\nAnswer:")
	for k in range(len(ans)):
		print('{:-7.2f}'.format(ans[k][0]), end=' ')
	print()
