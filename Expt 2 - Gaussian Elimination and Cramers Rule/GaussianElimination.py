# Solve system of linear equations using gaussian elimination and back substitution.

# Tapan Mayukh - 170121048 - 05/08/2019


def sort_by_zeros(A, b):
	n = len(A)
	var = [0 for _ in range(n)]
	
	for i in range(n):
		for j in range(n):
			if A[i][j] != 0:
				break
			var[i] += 1
	
	for i in range(n):
		if max(var) <= 0:
			break
		idx = var.index(max(var))
		
		A[n-i-1], A[idx] = A[idx], A[n-i-1]
		b[n-i-1], b[idx] = b[idx], b[n-i-1]
		
		var[idx] = -1
		var[n-i-1], var[idx] = var[idx], var[n-i-1]


def gaussian(A, b):
	assert(len(A) == len(A[0]))
	assert(len(A) == len(b))
	
	A = A[:]
	b = b[:]
	n = len(A)
	
	for i in range(n - 1):
		sort_by_zeros(A, b)
		ex = i
		
		for j in range(i + 1, n):
			if A[i][i] == 0 and A[j][i] != 0:
				ex = j
			if A[j][i] == 1:
				ex = j
		
		if ex != i:
			A[i], A[ex] = A[ex], A[i]
			b[i], b[ex] = b[ex], b[i]
		
		for j in range(i + 1, n):
			t = A[j][i] / A[i][i]
			
			for k in range(i, n):
				A[j][k] -= t * A[i][k]
			
			b[j][0] -= t * b[i][0]
		
			print()
			for j in range(n):
				for k in range(n):
					print('{:-7.2f}'.format(A[j][k]), end=' ')
				print('|| {:-7.2f}\n'.format(b[j][0]), end='')
		
	return A, b


def back_sub(A, b):
	n = len(A)
	
	det = 1
	for i in range(n):
		det *= A[i][i]
	
	if det == 0:
		assert(det != 0)
		print("A is a singular matrix i.e.\n\t2 or more lines in the system of equations are either coincident or parallel")
	
	ans = [0 for i in range(n)]
	for i in range(n-1, -1, -1):
		t = 0
		for j in range(i + 1, n):
			t += ans[j] * A[i][j]
		
		ans[i] = (b[i][0] - t) / A[i][i]
	
	return ans		


# a = [[2.0, 1.0, 1.0], [1.0, 3.0, 2.0], [-1.0, 1.0, 6.0]]
# b = [[5.0], [4.0], [4.0]]

a = [[1.0, 2.0, 3.0], [3.0, 1.0, 2.0], [2.0, 3.0, 1.0]]
b = [[14.0], [11.0], [11.0]]

red_A, red_b = gaussian(a, b)
ans = back_sub(red_A, red_b)

print()
for k in range(len(ans)):
	print('{:-7.2f}'.format(ans[k]), end=' ')
print()
