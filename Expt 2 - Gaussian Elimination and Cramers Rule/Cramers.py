# Solve system of linear equations using Cramer's rule.

# Tapan Mayukh - 170121048 - 05/08/2019


def del_matrix(mat, r, c):
	del_mat = [[0 for i in range(len(mat[0]) - 1)] for i in range(len(mat) - 1)]
	
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if i < r and j < c:
				del_mat[i][j] = mat[i][j]
			elif i < r and j > c:
				del_mat[i][j - 1] = mat[i][j]
			elif i > r and j < c:
				del_mat[i - 1][j] = mat[i][j]
			elif i > r and j > c:
				del_mat[i - 1][j - 1] = mat[i][j]
	
	return del_mat


def determinant(mat):
	assert(len(mat) == len(mat[0]))
	
	if len(mat) == 1:
		return mat[0][0]
	elif len(mat) == 2:
		return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
	
	det = 0
	
	for i in range(len(mat[0])):
		del_mat = del_matrix(mat, 0, i)
		det += pow(-1, i) * mat[0][i] * determinant(del_mat)
	
	return det


def replaced_mat(A, b, col):
	repl_mat = [[0 for i in range(len(A[0]))] for i in range(len(A))]
	
	for i in range(len(A)):
		for j in range(len(A[0])):
			if j == col:
				repl_mat[i][j] = b[i][0]
			else:
				repl_mat[i][j] = A[i][j]
	
	return repl_mat


def cramers(A, b):
	assert(len(A) == len(A[0]))
	assert(len(A) == len(b))

	det_A = determinant(A)
	print("det. for coff.: {}".format(det_A))
	assert(det_A != 0)
	
	n = len(A)
	ans = [0 for i in range(n)]
	
	for i in range(n):
		repl_mat = replaced_mat(A, b, i)
		det_var = determinant(repl_mat)
		print("det. for var {}: {}".format(i + 1, det_var))
		ans[i] = det_var / det_A
	
	return ans


# a = [[2.0, 1.0, 1.0], [1.0, 3.0, 2.0], [-1.0, 1.0, 6.0]]
# b = [[5.0], [4.0], [4.0]]

a = [[1.0, 2.0, 3.0], [3.0, 1.0, 2.0], [2.0, 3.0, 1.0]]
b = [[14.0], [11.0], [11.0]]

ans = cramers(a, b)

print()
for k in range(len(ans)):
	print('{:-7.2f}'.format(ans[k]), end=' ')
print()
